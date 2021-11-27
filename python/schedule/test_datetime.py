#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime



def get_next_run_time(**options):
    every = options.get('every', 1)
    timeUnit = options.get('unit', None)
    day = options.get('day', None)
    at = options.get('at', None)

    now = datetime.datetime.now()

    if at is not None:
        newHour = int(at.split(":")[0])
        newMinute = int(at.split(":")[1])
        print("Hour: %s, Min: %s" % (newHour, newMinute))

        curHour = now.hour
        curMin = now.minute
        curYear = now.year
        curMonth = now.month
        curDay = now.day
        weekday = now.weekday

        # Only supported timeunit is 'days' or 'weeks'
        if timeUnit not in ["days", "weeks"]:
            print("Only supported time unit is days and weeks for this schedule")
            return

        if timeUnit == "days":
            timeDelta = datetime.timedelta(days=every)
        elif timeUnit == "weeks":
            timeDelta = datetime.timedelta(weeks=every)

        futureTime = datetime.datetime(curYear, curMonth, curDay, newHour, newMinute)
        timeDelta = futureTime - now
        nextRunTime = now + timeDelta
        print("Future time: ", futureTime.strftime("%Y-%m-%d %H:%M:%S") )
        print("Now: %s | Next Run: %s | Time Delta: %s" %
          (now.strftime("%Y-%m-%d %H:%M:%S"),
           nextRunTime.strftime("%Y-%m-%d %H:%M:%S"), timeDelta))

        return


    if timeUnit == "seconds":
        timeDelta = datetime.timedelta(seconds=every)
    elif timeUnit == "minutes":
        timeDelta = datetime.timedelta(minutes=every)
    elif timeUnit == "hours":
        timeDelta = datetime.timedelta(hours=every)
    elif timeUnit == "days":
        timeDelta = datetime.timedelta(days=every)
    elif timeUnit == "weeks":
        timeDelta = datetime.timedelta(weeks=every)

    nextRunTime = now + timeDelta

    print("Now: %s | Next Run: %s | Time Delta: %s" %
          (now.strftime("%Y-%m-%d %H:%M:%S"),
           nextRunTime.strftime("%Y-%m-%d %H:%M:%S"), timeDelta))

    return nextRunTime


def main():
    seperator = "-------------------------------------------"
    print(seperator)
    print("Run a job every 3 seconds")
    schedule = {
        'every': 3,
        'unit': 'seconds',
        'at': None,
        'day': None
    }
    nextRun = get_next_run_time(**schedule)

    print(seperator)
    print("Run a job every 2 days")
    schedule = {
        'every': 2,
        'unit': 'days',
        'at': None,
        'day': None
    }
    nextRun = get_next_run_time(**schedule)


    print(seperator)
    print("Run a job every 2 weeks")
    schedule = {
        'every': 2,
        'unit': 'weeks',
        'at': None,
        'day': None
    }
    nextRun = get_next_run_time(**schedule)


    print(seperator)
    print("Run a job at 11:30 every 2 days")
    schedule = {
        'every': 2,
        'unit': 'days',
        'at': "11:30",
        'day': None
    }
    nextRun = get_next_run_time(**schedule)


    print(seperator)
    print("Run a job at 8:30 every 1 days")
    schedule = {
        'every': 1,
        'unit': 'days',
        'at': "8:30",
        'day': None
    }
    nextRun = get_next_run_time(**schedule)

    print(seperator)
    print("Run a job at 11:30 every 2 weeks")
    schedule = {
        'every': 2,
        'unit': 'weeks',
        'at': "11:30",
        'day': None
    }
    nextRun = get_next_run_time(**schedule)


if __name__ == '__main__':
    main()
