"""Perform date analytics on a list of dates provided by the user."""

from datetime import datetime, date

# constants
ERROR_EMPTY_DATE_LIST = "Date list cannot be empty"
ERROR_INVALID_DATE_FORMAT = "Invalid date format. Please try again."
ERROR_PREFIX = "Error : {}"
INPUT_DATE_PROMPT = "Enter dates in YYYY-MM-DD format : (0 to stop) "
INTERRUPT_MESSAGE = "Program was interrupted."
PRINT_EARLIEST = "earliest Date: "
PRINT_LATEST = "Latest Date: "
PRINT_UNIQUE = "Unique Dates: "


def get_date_analytics(
    raw_dates: list[str],
) -> tuple[date, date, set[date]]:
    """Find the earliest date, latest date and unique dates from a list of dates.

    Args:
        raw_dates : List of dates in string format YYYY-MM-DD.

    Raises:
        ValueError: When the input date list is empty.

    Returns:
        Earliest date, latest date and unique dates.
    """
    if not raw_dates:
        raise ValueError(ERROR_EMPTY_DATE_LIST)

    date_list: list[date] = []
    for d in raw_dates:
        date_list.append(datetime.fromisoformat(d).date())

    date_list.sort()
    date_set: set[date] = set(date_list)

    return date_list[0], date_list[-1], date_set


def get_valid_dates() -> list[str]:
    """Get valid dates from user input until '0' is entered.

    Raises:
        ValueError: When the date is invalid.

    Returns:
        List of valid dates in string format YYYY-MM-DD.
    """
    date_input: str = ""
    valid_dates: list[str] = []

    while date_input != "0":
        date_input = input(INPUT_DATE_PROMPT)
        if date_input == "0":
            break

        try:
            datetime.fromisoformat(date_input).date()
        except ValueError:
            print(ERROR_INVALID_DATE_FORMAT)
        else:
            valid_dates.append(date_input)

    return valid_dates


if __name__ == "__main__":
    try:
        dates = get_valid_dates()
        earliest, latest, unique = get_date_analytics(dates)

        print(PRINT_EARLIEST, earliest)
        print(PRINT_LATEST, latest)
        print(PRINT_UNIQUE, [d.isoformat() for d in unique])

    except KeyboardInterrupt:
        print(INTERRUPT_MESSAGE)

    except ValueError as e:
        print(ERROR_PREFIX.format(e))

    except Exception as ex:
        print(ERROR_PREFIX.format(ex))
