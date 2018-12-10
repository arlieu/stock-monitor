import datetime
from pytz import timezone


start_time = datetime.time(9, 30, 0, 0)
integer_start_time = \
    start_time.hour * 3600000000 + \
    start_time.minute * 60000000 + \
    start_time.second * 1000000 + \
    start_time.microsecond
end_time = datetime.time(16, 0, 0, 0)
integer_end_time = \
    end_time.hour * 3600000000 + \
    end_time.minute * 60000000 + \
    end_time.second * 1000000 + \
    end_time.microsecond


def get_current_date_time():
    tz = timezone("EST")
    return datetime.datetime.now(tz)


def is_trading_hours():
    current = get_current_date_time()
    if current.weekday() > 4:
        return False

    current_time = current.time()
    if start_time < current_time < end_time:
        return True

    return False


def wait_time():
    current = get_current_date_time()
    day = current.weekday()
    current_time = current.time()
    integer_current_time = \
        current_time.hour * 3600000000 + \
        current_time.minute * 60000000 + \
        current_time.second * 1000000 + \
        current_time.microsecond

    time_interval = 1800000000
    if integer_current_time < integer_start_time:
        time_interval = integer_start_time - integer_current_time
    elif integer_current_time > integer_end_time:
        time_interval = integer_start_time + (86400000000 - integer_current_time)

    if day-7 > -3:
        time_interval = abs(day-7) * 86400000000 + time_interval

    return time_interval
