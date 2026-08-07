# Contributing

Contributions that add missing solutions, correct existing solutions, or
improve the scraper and documentation are welcome.

## Before you start

- Search the existing issues and pull requests to avoid duplicate work.
- For a substantial change, open an issue before investing significant effort.
- Never commit beecrowd credentials, `.env` files, browser data, or other
  secrets.

## Adding or correcting a solution

1. Use the beecrowd problem ID as the file name and place the file in the
   matching thousand-wide directory. For example, problem `1001` belongs at
   `1000-1999/1001.py`.
2. Use `.py` for Python solutions and `.sql` for PostgreSQL solutions.
3. Submit code accepted by beecrowd for the corresponding problem.
4. Keep the solution self-contained and avoid unrelated changes.

Python solutions in this repository follow these conventions:

- Prefer `input()` and `print()` for input and output; do not use `sys` for them unless necessary.
- Put the script at the root of the file without a `main()` function or an
  `if __name__ == "__main__":` guard.
- When input continues until EOF, use a `while True` loop and handle
  `EOFError` to stop reading.
- Match the output format in the problem statement exactly.

## Scraper changes

Setup and usage instructions are in [`scraper/README.md`](scraper/README.md).
Use a test account or dry-run mode when possible, and make sure logs and error
messages cannot expose credentials.

## Pull requests

- Use a clear title that identifies the problem ID or component being changed.
- Explain what changed and why.
- Link related issues.
- Confirm that new or corrected solutions were accepted by beecrowd.
- Keep each pull request focused so it is easy to review.

By contributing, you agree that your contribution will be licensed under the
repository's [MIT License](LICENSE).
