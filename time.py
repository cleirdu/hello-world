import datetime

def time():
    """
    Returns the current date and time in the format "HH:MM MM/DD/YYYY".
    """
    current_time = datetime.datetime.now()
    formatted_datetime = current_time.strftime("%H:%M %m/%d/%Y")
    return formatted_datetime


if __name__ == '__main__':
    print(time())
