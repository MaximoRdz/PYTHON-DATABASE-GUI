import datetime as dt


def get_date():
    """
    Get current date.
    :return: tuple (year[int], month[int], day[int])
    """
    day = dt.date.today().day
    month = dt.date.today().month
    year = dt.date.today().year
    return year, month, day
