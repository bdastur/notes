#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime



def get_next_run_time(**options):
    days = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3,
            'friday': 4, 'saturday': 5, 'sunday': 6}

    init = options.get('init', True)
    every = options.get('every', 1)
    timeUnit = options.get('unit', None)
    day = options.get('day', None)
    at = options.get('at', None)

    now = datetime.datetime.now()

    #----------------------------------
    # Handling specific time.
    #----------------------------------
    if at is not None:
        newHour = int(at.split(":")[0])
        newMinute = int(at.split(":")[1])
        print("Hour: %s, Min: %s" % (newHour, newMinute))

        curHour = now.hour
        curMin = now.minute
        curYear = now.year
        curMonth = now.month
        curDay = now.day
        weekday = now.weekday()

        # Two supported options with 'at':
        # 1. 'day' - provide a specific day
        # 2.  every day - 'unit' day.

        if day is not None:
            dayDiff = (weekday - days[day] - 1) % 6
            futureMinutes = dayDiff * 24 * 60

            if newHour < curHour:
                futureMinutes = futureMinutes - ((curHour - newHour) * 60)
            else:
                futureMinutes = futureMinutes + ((newHour - curHour) * 60)

            if newMinute < curMin:
                futureMinutes = futureMinutes - (curMin - newMinute)
            elif newMinute > curMin:
                futureMinutes = futureMinutes + (newMinute - curMin)

            timeDelta = datetime.timedelta(minutes=futureMinutes)
            nextRunTime = now + timeDelta

            print("Now: %s | Next Run: %s | Time Delta: %s" %
                  (now.strftime("%Y-%m-%d %H:%M:%S"),
               nextRunTime.strftime("%Y-%m-%d %H:%M:%S"), timeDelta))
            return

        dayDiff = 1
        futureMinutes = dayDiff * 24 * 60
        if newHour < curHour:
            futureMinutes = futureMinutes - ((curHour - newHour) * 60)
        else:
            futureMinutes = futureMinutes + ((newHour - curHour) * 60)

        if newMinute < curMin:
            futureMinutes = futureMinutes - (curMin - newMinute)
        elif newMinute > curMin:
            futureMinutes = futureMinutes + (newMinute - curMin)

        timeDelta = datetime.timedelta(minutes=futureMinutes)
        nextRunTime = now + timeDelta

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
    print("Run a job at 11:30 every tuesday")
    schedule = {
        'every': 1,
        'unit': 'days',
        'at': "11:30",
        'day': 'tuesday'
    }
    nextRun = get_next_run_time(**schedule)

    print(seperator)
    print("Run a job at 11:45 every tuesday")
    schedule = {
        'every': 1,
        'unit': 'days',
        'at': "11:45",
        'day': 'tuesday'
    }
    nextRun = get_next_run_time(**schedule)

    print(seperator)
    print("Run a job at 20:45 every tuesday")
    schedule = {
        'every': 1,
        'unit': 'days',
        'at': "20:45",
        'day': 'tuesday'
    }
    nextRun = get_next_run_time(**schedule)

    print(seperator)
    print("Run a job at 20:45 every day")
    schedule = {
        'every': 1,
        'unit': 'days',
        'at': "20:45",
        'day': None
    }
    nextRun = get_next_run_time(**schedule)

    print(seperator)
    print("Run a job at 8:25 every day")
    schedule = {
        'every': 1,
        'unit': 'days',
        'at': "8:25",
        'day': None
    }
    nextRun = get_next_run_time(**schedule)


if __name__ == '__main__':
    main()
