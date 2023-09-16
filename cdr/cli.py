import click
import os
from rich.console import Console

console = Console()

@click.command()
@click.option('-c', '--count-files', is_flag=True, help="Count CSV/TSV files instead of rows.")
@click.option('-b', '--blank', is_flag=True, help="Count blank/non-parsable CSV/TSV files.")
@click.option('-l', '--readable', is_flag=True, help="Show numbers in a more readable format.")
@click.argument('dir', required=False, default='.')
def cli(count_files, blank, readable, dir):
    """
    cdr: A CLI tool for counting rows, columns, and files in CSV/TSV datasets.
    """
    total_rows = 0
    total_files = 0
    total_blank_files = 0

    # Loop through each CSV/TSV file in the directory
    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith(('.csv', '.tsv')):
                total_files += 1
                filepath = os.path.join(root, file)

                if blank:
                    # Count blank or broken files
                    if os.path.getsize(filepath) == 0:
                        total_blank_files += 1
                else:
                    # Count the number of rows in each file
                    with open(filepath, 'r') as f:
                        file_rows = sum(1 for line in f) - 1  # Exclude header
                        total_rows += file_rows

    if count_files:
        output = f"CSV/TSV files found: {total_files}"
    elif blank:
        output = f"CSV/TSV blank or broken files found: {total_blank_files}"
    else:
        output = f"CSV/TSV rows: {total_rows}"

    if readable:
        output = output.replace(",", "")  # Remove commas for now; can use a more advanced formatter later

    console.print(output)

if __name__ == "__main__":
    cli()
