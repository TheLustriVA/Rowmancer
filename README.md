# RowMancer: CSV/TSV Data Reporter

![CDR_banner](assets/RowMancer_Banner.png)

## Description

`RowMancer` is a Command Line Interface (CLI) tool that allows you to count rows, columns, and files in CSV/TSV datasets. The tool provides various options for specific count metrics, including the ability to count blank files, specify directory depth, and calculate column statistics.

## License

This project is under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more details.

## Installation

### From Source

1. Clone the repository

    ```bash
    git clone https://github.com/TheLustriVA/Rowmancer.git
    ```

2. Navigate to the project directory

    ```bash
    cd RowMancer
    ```

3. Install the package

    ```bash
    pip install .
    ```

### From PyPI

You can also install the package from PyPI (once it's published):

```bash
pip install RowMancer

```

## Usage

Run the tool with no options to count all rows in all `.csv` and `.tsv` files in the current directory and its subdirectories:

```bash
Rowmancer
```

### Options

1. Count Files: `-c, --count-files`
    - Count the number of `.csv` and `.tsv` files instead of rows.

    ```bash
    RowMancer --count-files
    ```

2. Blank Files: `-b, --blank`
    - Count the number of blank or non-parsable `.csv` and `.tsv` files.

    ```bash
    RowMancer --blank
    ```

3. Readable Numbers: `-l, --readable`
    - Show numbers in a more readable format (e.g., 1,000 instead of 1000).

    ```bash
    RowMancer --readable
    ```

4. Directory: `dir`
    - Specify the directory to start the search.

    ```bash
    RowMancer /path/to/directory
    ```

5. Header Row: `-H, --header-row`
    - Exclude the first row from each `.csv` file in the count.

    ```bash
    RowMancer --header-row
    ```

6. Depth: `-d, --depth`
    - Set the directory depth for the search.

    ```bash
    RowMancer --depth 2
    ```

7. Column Stats: `-x, --columns`
    - Show column statistics (MIN, MAX, MEAN, SINGLE).

    ```bash
    RowMancer --columns MIN
    ```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Author

- **KGB aka Marco Lustri** - *With help from GPT-4*

## Acknowledgments

- Morgan Medici, who knows more than most have forgotten.
