# beecrowd accepted-solutions scraper

Downloads accepted Python 3 submissions that do not already have a solution in
this repository.

## Setup

```bash
cd scraper
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
```

Fill in `BEECROWD_EMAIL` and `BEECROWD_PASSWORD` in `.env`, then run:

```bash
python scrape.py
```

Useful options:

```bash
python scrape.py --headed
python scrape.py --max-pages 3
python scrape.py --dry-run
python scrape.py --codes 3047,3053,3102
```

`--codes` restricts the scraper to the listed problem codes and overwrites their
existing solution files. This is useful for replacing previously corrupted
downloads.
