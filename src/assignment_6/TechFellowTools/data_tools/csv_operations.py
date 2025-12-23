"""Functions to process the CSV data in format of list[dict[str,str]]."""

import csv
from pathlib import Path


def read_csv(filepath: Path) -> list[dict[str, str]]:
    """Convert CSV data to list of dictionaries.

    Args:
        filepath: CSV file path.

    Returns:
        One dictionary per row, keyed by column headers.
    """
    with open(filepath, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_csv(filepath: Path, rows: list[dict[str, str]]) -> None:
    """Write the data to CSV file.

    Args:
        filepath: CSV destination file path.
        rows: Rows to be written to the CSV file.
    """
    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def filter_rows(rows: list[dict[str, str]], key: str, value: str) -> list[dict[str, str]]:
    """Filter the CSV data to fetch the specific row.

    Args:
        rows: CSV file content.
        key: Key to be searched.
        value: Matching value for the key to be searched.

    Returns:
        The row with the matching key and values.
    """
    return list(filter(lambda row: row.get(key) == value, rows))


def select_columns(rows: list[dict[str, str]], columns: list[str]):
    """Select the column and return all the row in the column.

    Args:
        rows: CSV file content.
        columns: Column to be extracted.

    Returns:
        Extracted column.
    """
    return [{col: row[col] for col in columns if col in row} for row in rows]


def sort_rows(rows: list[dict[str, str]], key: str):
    """Sort the rows based on the mentioned key.

    Args:
        rows: CSV file content.
        key: The key based on which the rows should be sorted.

    Returns:
        Sorted rows based on the key provided.
    """
    return sorted(rows, key=lambda x: x.get(key, ""))
