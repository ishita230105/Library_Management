from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

def parse_date(date_str):
    """Converts string to datetime object. Returns None if invalid."""
    try:
        return datetime.strptime(date_str, DATE_FORMAT)
    except ValueError:
        return None

def input_date(prompt="Enter date (YYYY-MM-DD): "):
    """Keeps prompting until a valid date is entered."""
    while True:
        date_str = input(prompt).strip()
        date_obj = parse_date(date_str)
        if date_obj:
            return date_obj
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")

def days_between(start, end):
    """Returns number of days between two datetime objects."""
    return (end - start).days

def print_line(char="-", length=40):
    print(char * length)
