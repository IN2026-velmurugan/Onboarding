"""Module to perform date analytics on a list of dates provided by the user.
"""

from datetime import datetime
from typing import List, Set, Tuple


def date_analytics(
    date_list_string: List[str],
) -> Tuple[datetime, datetime, Set[datetime]]:
    """To find the earliest date, latest date and unique dates from a list of dates.

    Args:
        date_list (List[str]): list of dates in string format YYYY-MM-DD

    Returns:
        Tuple[datetime, datetime, Set[datetime]]: earliest date, latest date and unique dates
    """
    date_list: List[datetime] = []
    for date in date_list_string:
        date_list.append(datetime.strptime(date, "%Y-%m-%d"))
    date_list.sort()
    date_set: Set[datetime] = set(date_list)
    print(date_list)
    return date_list[0], date_list[-1], date_set


def validate_date(date_string: str) -> bool:
    """To validate date string format YYYY-MM-DD.

    Args:
        date_string (str): date in string format

    Returns:
        bool: true if valid, false otherwise
    """
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except Exception:
        return False


def get_valid_dates() -> List[str]:
    """To get valid dates from user input until '0' is entered.

    Returns:
        List[str]: list of valid dates in string format YYYY-MM-DD
    """
    date: str = ""
    valid_dates: List[str] = []
    while date != "0":
        date = input("Enter dates in YYYY-MM-DD format : (0 to stop) ")
        if validate_date(date):
            valid_dates.append(date)
        elif date == "0":
            break
        else:
            print("Invalid date format. Please try again.")
    return valid_dates


if __name__ == "__main__":
    dates = get_valid_dates()
    Earliest, latest, unique = date_analytics(dates)
    print("Earliest Date: ", datetime.strftime(Earliest, "%Y-%m-%d"))
    print("Latest Date: ", datetime.strftime(latest, "%Y-%m-%d"))
    print("Unique Dates: ", [datetime.strftime(date, "%Y-%m-%d") for date in unique])
