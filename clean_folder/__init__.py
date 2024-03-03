import datetime


# def check_format(date):


def get_days_from_today(date):

    # try to convert string to datetime format
    try:
        parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d")

    except ValueError:
        return "Incorrect date input. Please enter the date following the example: 2021-05-27."

    # find today date
    today_date = datetime.datetime.now()

    # сalculate the difference between 2 days
    difference = today_date - parsed_date

    # return the difference between days
    return difference.days


print(get_days_from_today("2010-15-07"))
