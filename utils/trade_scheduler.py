import datetime
from pytz import timezone
import schedule


startTime = datetime.time(9, 30, 0, 0)
integerStartTime = \
    startTime.hour * 3600000000 + \
    startTime.minute * 60000000 + \
    startTime.second * 1000000 + \
    startTime.microsecond
endTime = datetime.time(16, 0, 0, 0)
integerEndTime = \
    endTime.hour * 3600000000 + \
    endTime.minute * 60000000 + \
    endTime.second * 1000000 + \
    endTime.microsecond


def getCurrentDateTime():
    tz = timezone("EST")
    return datetime.datetime.now(tz)


def isTradingHours():
    current = getCurrentDateTime()
    if current.weekday() > 4:
        return False

    currentTime = current.time()
    if currentTime > startTime and currentTime < endTime:
        return True

    return False


def waitTime():
    current = getCurrentDateTime()
    day = current.weekday()
    currentTime = current.time()
    integerCurrentTime = \
        currentTime.hour * 3600000000 + \
        currentTime.minute * 60000000 + \
        currentTime.second * 1000000 + \
        currentTime.microsecond

    dayInterval = abs(day-7) * 86400000000
    timeInterval = 3600000000
    if currentTime < startTime:
        timeInterval = int(integerStartTime)-int(integerCurrentTime)
    elif currentTime > endTime:
        timeInterval = int(integerStartTime+(86400000000-integerCurrentTime))

    return timeInterval
