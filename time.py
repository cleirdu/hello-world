import datetime

def time():
    current_time = datetime.datetime.now()
    formatted_datetime = current_time.strftime("%H:%M %m/%d/%Y")
    return formatted_datetime


if __name__ == '__main__':
    print(time())
