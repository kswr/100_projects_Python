import datetime as dt


def ageInSeconds(year, month, day):
    """Type your birthdate to get your age in seconds"""
    return (dt.datetime.now() - dt.datetime(year, month, day)).total_seconds()


print(ageInSeconds(1994, 5, 8))

