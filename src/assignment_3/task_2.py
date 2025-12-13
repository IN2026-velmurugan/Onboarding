import re
from typing import List, Set
from datetime import datetime


def date_analytics(DateList : List[str]):
    date_list : List[datetime] = []
    for date in DateList:
        date_list.append(datetime.strptime(date, "%Y-%m-%d"))
    date_list.sort()
    date_set : Set[datetime]= set(date_list)
    print(date_list)
    return date_list[0], date_list[-1], date_set

def validate_date(date_string: str) -> bool:
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except:
        return False
    
def get_valid_dates() -> List[str]:
    date : str = ""
    valid_dates : List[str] = []
    while date != "0":
        date = input("Enter dates in YYYY-MM-DD format : (0 to stop) ")
        if validate_date(date):
            valid_dates.append(date)
        else:
            print("Invalid date format. Please try again.")
    return valid_dates
    
if __name__ == "__main__":
    dates = get_valid_dates()
    Earliest, latest, unique = date_analytics(dates)
    print("Earliest Date: ",datetime.strftime(Earliest, "%Y-%m-%d"))
    print("Latest Date: ",datetime.strftime(latest, "%Y-%m-%d"))
    print("Unique Dates: ",[datetime.strftime(date, "%Y-%m-%d") for date in unique])