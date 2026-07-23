from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

from dotenv import load_dotenv
from playwright.sync_api import Locator, Page, sync_playwright
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


BASE_URL = "https://judge.beecrowd.com"
LOGIN_URL = f"{BASE_URL}/pt/login"
RUNS_URL = f"{BASE_URL}/pt/runs?answer_id=1&page={{page}}"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
console = Console()


@dataclass(frozen=True)
class Submission:
    problem: str
    language: str
    code_url: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download missing accepted Python 3 solutions from beecrowd."
    )
    parser.add_argument(
        "--headed", action="store_true", help="Show the browser while scraping."
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        help="Stop after this many runs pages (default: continue to the last page).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List eligible submissions without downloading them.",
    )
    return parser.parse_args()


def credentials() -> tuple[str, str]:
    load_dotenv(Path(__file__).resolve().parent / ".env")
    email = os.getenv("BEECROWD_EMAIL")
    password = os.getenv("BEECROWD_PASSWORD")
    if not email or not password:
        raise RuntimeError(
            "Set BEECROWD_EMAIL and BEECROWD_PASSWORD in scraper/.env."
        )
    return email, password


def existing_problem_codes() -> set[str]:
    return {
        path.stem
        for path in PROJECT_ROOT.glob("[0-9]*-[0-9]*/*.py")
        if path.stem.isdigit()
    }


def solution_path(problem: str) -> Path:
    number = int(problem)
    range_start = (number // 1000) * 1000
    range_end = range_start + 999
    return PROJECT_ROOT / f"{range_start}-{range_end}" / f"{problem}.py"


def login(page: Page, email: str, password: str) -> None:
    with console.status("[bold cyan]Signing in to beecrowd…", spinner="dots"):
        page.goto(LOGIN_URL, wait_until="domcontentloaded")
        page.locator("#email").fill(email)
        page.locator("#password").fill(password)

        remember_me = page.locator("#remember-me")
        if remember_me.count():
            remember_me.check()

        page.locator("#submit-btn").click()
        page.wait_for_url(re.compile(r"https://judge\.beecrowd\.com/pt/?$"))
    console.print("[bold green]✓[/] Signed in successfully")


def text_in_column(row: Locator, index: int) -> str:
    return row.locator("td").nth(index).inner_text().strip()


def submissions_on_page(page: Page, page_number: int) -> list[Submission]:
    page.goto(RUNS_URL.format(page=page_number), wait_until="domcontentloaded")
    rows = page.locator("#element table tbody tr")
    if not rows.count():
        rows = page.locator("#element tbody tr")

    submissions: list[Submission] = []
    for index in range(rows.count()):
        row = rows.nth(index)
        columns = row.locator("td")
        if columns.count() < 6:
            continue

        code_link = columns.nth(0).locator('a[href*="/pt/runs/code/"]').first
        problem_link = columns.nth(2).locator("a").first
        if not code_link.count() or not problem_link.count():
            continue

        problem = problem_link.inner_text().strip()
        language = text_in_column(row, 5)
        href = code_link.get_attribute("href")
        if not problem.isdigit() or not href:
            continue

        submissions.append(
            Submission(
                problem=problem,
                language=language,
                code_url=urljoin(BASE_URL, href),
            )
        )
    return submissions


def fetch_code(page: Page, submission: Submission) -> str:
    page.goto(submission.code_url, wait_until="domcontentloaded")
    code = page.locator(".ace_scroller pre#code")
    if not code.count():
        code = page.locator("pre#code")
    code.wait_for(state="visible")
    return code.inner_text().replace("\r\n", "\n").rstrip() + "\n"


def scrape(page: Page, max_pages: int | None, dry_run: bool) -> int:
    existing = existing_problem_codes()
    selected: set[str] = set()
    downloaded = 0
    stats: Counter[str] = Counter()
    page_number = 1

    console.print(
        f"[dim]Found {len(existing)} existing Python solution(s) in the repository.[/]"
    )

    while max_pages is None or page_number <= max_pages:
        with console.status(
            f"[cyan]Scanning accepted runs — page {page_number}…", spinner="bouncingBar"
        ):
            submissions = submissions_on_page(page, page_number)
        if not submissions:
            console.print("[yellow]◇[/] No more runs found; reached the last page.")
            break

        python_submissions = [
            submission
            for submission in submissions
            if "Python 3" in submission.language
        ]
        eligible = [
            submission
            for submission in python_submissions
            if submission.problem not in existing
            and submission.problem not in selected
        ]
        stats["runs"] += len(submissions)
        stats["python"] += len(python_submissions)
        stats["eligible"] += len(eligible)
        stats["skipped"] += len(python_submissions) - len(eligible)

        for submission in eligible:
            selected.add(submission.problem)
            destination = solution_path(submission.problem)
            if dry_run:
                console.print(
                    f"[bold magenta]◎ DRY RUN[/] [bold]{submission.problem}[/] "
                    f"[dim]← {submission.code_url}[/]"
                )
                continue

            with console.status(
                f"[cyan]Downloading problem {submission.problem}…", spinner="dots"
            ):
                code = fetch_code(page, submission)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(code, encoding="utf-8")
            existing.add(submission.problem)
            downloaded += 1
            console.print(
                f"[bold green]✓ SAVED[/] [bold]{submission.problem}[/] "
                f"[dim]→ {destination.relative_to(PROJECT_ROOT)}[/]"
            )

        console.print(
            f"[blue]◆ PAGE {page_number}[/]  "
            f"[bold]{len(submissions)}[/] runs  •  "
            f"[green]{len(python_submissions)}[/] Python 3  •  "
            f"[yellow]{len(eligible)}[/] new"
        )
        page_number += 1

    stats["downloaded"] = downloaded
    show_summary(stats, dry_run)
    return downloaded


def show_summary(stats: Counter[str], dry_run: bool) -> None:
    table = Table.grid(padding=(0, 2))
    table.add_column(style="dim")
    table.add_column(justify="right", style="bold")
    table.add_row("Accepted runs inspected", str(stats["runs"]))
    table.add_row("Python 3 submissions", str(stats["python"]))
    table.add_row("Already present / duplicate", str(stats["skipped"]))
    table.add_row(
        "Would download" if dry_run else "Solutions downloaded",
        str(stats["eligible"] if dry_run else stats["downloaded"]),
    )
    console.print(Panel(table, title="[bold cyan]Scrape complete[/]", border_style="cyan"))


def main() -> int:
    args = parse_args()
    if args.max_pages is not None and args.max_pages < 1:
        console.print(
            "[bold red]Error:[/] --max-pages must be greater than zero.",
        )
        return 2

    try:
        mode = "DRY RUN" if args.dry_run else "DOWNLOAD"
        console.print(
            Panel.fit(
                "[bold cyan]beecrowd Solution Scraper[/]\n"
                f"[dim]{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  •  {mode}[/]",
                border_style="bright_blue",
            )
        )
        email, password = credentials()
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=not args.headed)
            context = browser.new_context()
            page = context.new_page()
            login(page, email, password)
            scrape(page, args.max_pages, args.dry_run)
            browser.close()
        return 0
    except Exception as error:
        console.print(f"\n[bold red]✗ Scraper failed:[/] {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
