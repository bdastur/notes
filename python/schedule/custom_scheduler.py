#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import functools
import time


def test_job(**kwargs):
    print("Running test job with kwargs: ", kwargs)
    time.sleep(3)
    return "Data from testjob"


class Scheduler():
    def __init__(self):
        self.jobs = []

    def scheule_job(self, **options):
        job = Job(**options)
        self.jobs.append(job)

    def run_pending(self):
        schedulableJobs = [job for job in self.jobs if job.is_schedulable()]
        print("[%d] Schedulable jobs: %s " % (len(schedulableJobs), schedulableJobs))
        for job in schedulableJobs:
            job.run()





class Job():
    def __init__(self, **options):
        schedule = options['schedule']
        every = schedule.get('every', 1)
        unit = schedule.get('unit', 'seconds')
        print("Job init: Unit: %s, Every: %d " % (unit, every))
        jobOptions = options['jobOptions']
        jobFunction = options['jobFunction']
        self.job_func = functools.partial(jobFunction, **jobOptions)

        now = datetime.datetime.now()
        self.timeDelta = datetime.timedelta(seconds=every)
        self.schedulableTime = now + self.timeDelta
        print("Schedulable time: ", self.schedulableTime)
        print("type: ", type(self.schedulableTime))

    def is_schedulable(self):
        now = datetime.datetime.now()
        if now >= self.schedulableTime:
            print("Curr time: %s, Scheduleable time: %s" %
                  (now.strftime("%Y-%m-%d %H:%M:%S"),
                   self.schedulableTime.strftime("%Y-%m-%d %H:%M:%S")))
            return True

        return False

    def run(self):
        print("Do something")
        now = datetime.datetime.now()
        self.schedulableTime = now + self.timeDelta
        print("Now: %s, Next run: %s" % (now.strftime("%Y-%m-%d %H:%M:%S"),
                   self.schedulableTime.strftime("%Y-%m-%d %H:%M:%S")))
        ret = self.job_func()
        print("Returned data: ", ret)
        time.sleep(2)



def main():
    # User input.
    # Define a job:
    # Run every minute.
    scheduler = Scheduler()

    options = {
        'schedule': {
            'every': 10,
            'unit': 'seconds'
        },
        'jobFunction': test_job,
        'jobOptions': {
          'apikey': 'ALKFLLL',
          'session': 'test'
        }
    }
    scheduler.scheule_job(**options)

    options = {
        'schedule': {
            'every': 10,
            'unit': 'seconds'
        },
        'jobFunction': test_job,
        'jobOptions': {
          'apikey': 'ALKFLLL',
          'session': 'test'
        }
    }
    scheduler.scheule_job(**options)

    for x in range(50):
        scheduler.run_pending()
        time.sleep(2)



if __name__ == '__main__':
    main()
