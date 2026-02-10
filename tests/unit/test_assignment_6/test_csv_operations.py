"""Tests for CSV operations in TechFellowTools data_tools module."""

import csv
from pathlib import Path

import pytest
from src.assignment_6.TechFellowTools.data_tools.csv_operations import (
    filter_rows,
    read_csv,
    select_columns,
    sort_rows,
    write_csv,
)

CSV_PATH = r"sample.csv"


@pytest.fixture
def sample_csv_file():
    rows = [
        {"name": "Alice", "age": "30", "city": "New York"},
        {"name": "Bob", "age": "25", "city": "Los Angeles"},
        {"name": "Charlie", "age": "35", "city": "Chicago"},
        {"name": "Clare", "age": "25"},
    ]

    path = Path(CSV_PATH)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    yield path

    path.unlink(missing_ok=True)


@pytest.fixture
def sample_csv_file_header_only():
    headers = ["name", "age", "city"]
    path = Path(CSV_PATH)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

    yield path

    path.unlink(missing_ok=True)


@pytest.fixture
def empty_csv_file():
    path = Path(CSV_PATH)

    with path.open("w", newline="", encoding="utf-8"):
        pass

    yield path

    path.unlink(missing_ok=True)


@pytest.mark.parametrize(
    "fixture_name, expected_output",
    [
        (
            "sample_csv_file",
            [
                {"name": "Alice", "age": "30", "city": "New York"},
                {"name": "Bob", "age": "25", "city": "Los Angeles"},
                {"name": "Charlie", "age": "35", "city": "Chicago"},
                {"name": "Clare", "age": "25", "city": ""},
            ],
        ),
        ("sample_csv_file_header_only", []),
    ],
)
def test__read_csv__valid_file__returns_data_as_list_of_dicts(
    fixture_name, expected_output, request
):
    filepath = request.getfixturevalue(fixture_name)
    answer = read_csv(filepath)

    assert expected_output == answer


def test__read_csv__file_not_found__raises_file_not_found_error():
    file_path = Path("non_existent_file.csv")

    with pytest.raises(FileNotFoundError):
        read_csv(file_path)


def test__write_csv__valid_input__writes_data_to_csv(empty_csv_file):
    filepath = empty_csv_file
    rows = [
        {"name": "David", "age": "28", "city": "Miami"},
        {"name": "Eva", "age": "22", "city": "Boston"},
    ]

    write_csv(filepath, rows)
    with filepath.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        written_rows = list(reader)

    assert rows == written_rows


def test__write_csv__empty_rows__raises_index_error(empty_csv_file):
    filepath = empty_csv_file
    rows = []

    with pytest.raises(IndexError):
        write_csv(filepath, rows)


def test__filter_rows__valid_values__returns_filtered_rows(sample_csv_file):
    rows = read_csv(sample_csv_file)
    filtered_rows = [row for row in rows if row["city"] == "Chicago"]

    answer = filter_rows(rows, "city", "Chicago")

    assert filtered_rows == answer


@pytest.mark.parametrize(
    "fixture_name, key, value",
    [
        ("sample_csv_file", "city", "texas"),
        ("sample_csv_file", "dob", "25-10-2004"),
        ("sample_csv_file_header_only", "name", "Alice"),
        ("sample_csv_file_header_only", "", "Alice"),
        ("sample_csv_file_header_only", None, "Alice"),
    ],
)
def test__filter_rows__invalid_params__returns_empty_list(fixture_name, key, value, request):
    rows = read_csv(request.getfixturevalue(fixture_name))

    answer = filter_rows(rows, key, value)

    assert answer == []


@pytest.mark.parametrize(
    "key",
    [
        (["city"]),
        (["age", "name"]),
    ],
)
def test__select_columns__valid_columns__returns_selected_columns(sample_csv_file, key):
    rows = read_csv(sample_csv_file)
    columns = key
    selected_columns = [{col: row[col] for col in columns} for row in rows]

    answer = select_columns(rows, columns)

    assert selected_columns == answer


@pytest.mark.parametrize(
    "fixture_name, key",
    [
        ("sample_csv_file", "dob"),
        ("sample_csv_file", ""),
        ("sample_csv_file", None),
        ("sample_csv_file_header_only", "name"),
    ],
)
def test__select_columns__invalid_parameters__returns_empty(fixture_name, key, request):
    rows = read_csv(request.getfixturevalue(fixture_name))
    columns = [key]
    expected_output = [{} for _ in rows]

    answer = select_columns(rows, columns)

    assert expected_output == answer


def test__sort_rows__valid_key__returns_sorted_rows(sample_csv_file):
    rows = read_csv(sample_csv_file)
    key = "age"
    sorted_rows = sorted(rows, key=lambda row: row[key])

    answer = sort_rows(rows, key)

    assert sorted_rows == answer
