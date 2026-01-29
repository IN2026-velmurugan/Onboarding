"""Module contains the methods to process the CSV file or CSV data in format List[Dict[str,str]]."""

import csv
from typing import List, Dict


def read_csv(filepath: str) -> List[Dict[str, str]]:
    """Reads the CSV content of the file.

    Args:
        filepath: CSV file path.

    Returns:
        CSV date as list of columns matched to the CSV data.
    """
    with open(filepath, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_csv(filepath: str, rows: List[Dict[str, str]]) -> None:
    """Writes the CSV data to the file.

    Args:
        filepath: CSV destination file path.
        rows: Rows to be written to the CSV file.
    """
    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def filter_rows(rows: List[Dict[str, str]], key: str, value: str):
    """Searches the CSV and fetches the row data.

    Args:
        rows: CSV file content.
        key: Key to be searched.
        value: Matching value for the key to be searched.

    Returns:
        The row with the matching key and values.
    """
    return [row for row in rows if row.get(key) == value]


def select_columns(rows: List[Dict[str, str]], columns: List[str]):
    """Selects the column and returns all the row in the column.

    Args:
        rows: CSV file content.
        columns: Column to be extracted.

    Returns:
        Extracted column.
    """
    return [{col: row[col] for col in columns if col in row} for row in rows]


def sort_rows(rows: List[Dict[str, str]], key: str):
    """Sorts the rows based on the mentioned key.

    Args:
        rows: CSV file content.
        key: The key based on which the rows should be sorted.

    Returns:
        Sorted rows based on the key provided.
    """
    return sorted(rows, key=lambda x: x.get(key, ""))
