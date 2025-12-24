"""Perform date analytics on a list of dates provided by the user."""

from datetime import datetime


def get_date_analytics(
    raw_dates: list[str],
) -> tuple[datetime, datetime, set[datetime]]:
    """Find the earliest date, latest date and unique dates from a list of dates.

    Args:
        raw_dates : list of dates in string format YYYY-MM-DD.

    Raises:
        ValueError: When the input date list is empty.

    Returns:
        Earliest date, latest date and unique dates.
    """
    if not raw_dates:
        raise ValueError("Date list cannot be empty")

    date_list: list[datetime] = []
    for date in raw_dates:
        date_list.append(datetime.strptime(date, "%Y-%m-%d"))

    date_list.sort()
    date_set: set[datetime] = set(date_list)

    return date_list[0], date_list[-1], date_set


def validate_date(date_string: str) -> bool:
    """Validate whether the date string is in the format YYYY-MM-DD.

    Args:
        date_string : Date in string format.

    Returns:
        True if the date is valid, False otherwise.
    """
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        return False
    else:
        return True


def get_valid_dates() -> list[str]:
    """Get valid dates from user input until '0' is entered.

    Returns:
        list of valid dates in string format YYYY-MM-DD.
    """
    date: str = ""
    valid_dates: list[str] = []
    while date != "0":
        try:
            date = input("Enter dates in YYYY-MM-DD format : (0 to stop) ")
            if date == "0":
                break
            elif validate_date(date):
                valid_dates.append(date)
            else:
                print("Invalid date format. Please try again.")
        except KeyboardInterrupt:
            raise
    return valid_dates


if __name__ == "__main__":
    try:
        dates = get_valid_dates()
        earliest, latest, unique = get_date_analytics(dates)
        print("earliest Date: ", datetime.strftime(earliest, "%Y-%m-%d"))
        print("Latest Date: ", datetime.strftime(latest, "%Y-%m-%d"))
        print("Unique Dates: ", [datetime.strftime(date, "%Y-%m-%d") for date in unique])
    except ValueError as value_ex:
        print(f"Value_error : {value_ex}")
    except KeyboardInterrupt:
        print("Program was interrupted.")
    except Exception as ex:
        print(f"Error : {ex}")
