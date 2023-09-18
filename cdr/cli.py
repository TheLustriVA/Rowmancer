
import csv
import click
import os

@click.command()
@click.option(
    "-c", "--count-files", is_flag=True, help="Count CSV/TSV files instead of rows."
)
@click.option(
    "-b", "--blank", is_flag=True, help="Count blank/non-parsable CSV/TSV files."
)
@click.option(
    "-l", "--readable", is_flag=True, help="Show numbers in a more readable format."
)
@click.argument("dir", required=False, default=".")
@click.option(
    "-H",
    "--header-row",
    is_flag=True,
    help="Flags that you want the first row of each CSV file counted as a header row and removed from the count.",
)
@click.option(
    "-d",
    "--depth",
    type=int,
    help="Sets the directory depth that cdr will continue searching for CSV files.",
)
@click.option(
    "-x",
    "--columns",
    type=click.Choice(["MIN", "MAX", "MEAN", "SINGLE"]),
    help="Flag that you want the output to show the minimum, maximum, mean/average number of columns for those found, or the number of single-column files.",
)
def cli(count_files, header_row, blank, readable, dir, depth, columns):
    """
    cdr: A CLI tool for counting rows, columns, and files in CSV/TSV datasets.
    """
    total_rows = 0
    total_files = 0
    total_blank_files = 0

    def rel_depth(path):
        return len(os.path.relpath(path, dir).split(os.sep)) - 1

    column_stats = []

    def calc_column_metrics():
        if columns == "MIN":
            return min(column_stats)
        elif columns == "MAX":
            return max(column_stats)
        elif columns == "MEAN":
            return sum(column_stats) / len(column_stats)
        elif columns == "SINGLE":
            return sum(1 for x in column_stats if x == 1)

    for root, _, files in os.walk(dir):
        if depth is not None and rel_depth(root) > depth:
            continue

        for file in files:
            if file.endswith((".csv", ".tsv")):
                total_files += 1
                filepath = os.path.join(root, file)

                if blank:
                    if os.path.getsize(filepath) == 0:
                        total_blank_files += 1

                else:
                    with open(filepath, "r") as f:
                        csv_reader = csv.reader(f)
                        file_rows = 0
                        for row in csv_reader:
                            num_columns = len(row)
                            column_stats.append(num_columns)
                            file_rows += 1
                        if header_row:
                            file_rows -= 1
                        total_rows += file_rows

    output = ""
    if columns:
        output = f"CSV/TSV {columns.lower()} columns: {calc_column_metrics()}"
    elif count_files:
        output = f"CSV/TSV files found: {total_files}"
    elif blank:
        output = f"CSV/TSV blank or broken files found: {total_blank_files}"
    else:
        output = f"CSV/TSV rows: {total_rows}"

    if readable:
        output = output.replace(f"CSV/TSV rows: {total_rows}", f"CSV/TSV rows: {total_rows:,}")

    print(output)


if __name__ == "__main__":
    cli()
