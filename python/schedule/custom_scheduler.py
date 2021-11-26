#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import functools
import random
import time
import threading


def test_job(**kwargs):
    randval = random.randint(1, 10)
    msg = "Task will run for %d seconds args: (%s)" % (randval, kwargs)
    print(msg)
    time.sleep(randval)
    return "Data returned %d" % randval 


class Scheduler():
    def __init__(self):
        self.jobs = []

    def schedule_job(self, **options):
        job = Job(**options)
        self.jobs.append(job)

    def run_pending(self):
        schedulableJobs = [job for job in self.jobs if job.is_schedulable()]
        print("[%d] Schedulable jobs: %s " % (len(schedulableJobs), schedulableJobs))
        for job in schedulableJobs:
            job.run()



class Job():
    def __init__(self, **options):
        self.operation = options['operation']
        schedule = options['schedule']
        every = schedule.get('every', 1)
        unit = schedule.get('unit', 'seconds')
        print("Job init: Every: %d %s " % (every, unit))
        jobOptions = options['jobOptions']
        jobFunction = options['jobFunction']
        self.job_func = functools.partial(jobFunction, **jobOptions)

        now = datetime.datetime.now()
        if unit == "seconds":
            self.timeDelta = datetime.timedelta(seconds=every)
        elif unit == "minutes":
            self.timeDelta = datetime.timedelta(minutes=every)

        self.schedulableTime = now + self.timeDelta
        print("[%s] Next run scheduled: %s " % (self.operation, self.schedulableTime))

    def is_schedulable(self):
        now = datetime.datetime.now()
        if now >= self.schedulableTime:
            print("[%s] schedulable Curr time: %s, Scheduleable time: %s" %
                  (self.operation, now.strftime("%Y-%m-%d %H:%M:%S"),
                   self.schedulableTime.strftime("%Y-%m-%d %H:%M:%S")))
            return True

        return False

    def threadedRun(self):
        startTime = datetime.datetime.now()
        self.schedulableTime = startTime + self.timeDelta
        ret = self.job_func()
        endTime = datetime.datetime.now()
        elapsedSeconds = (endTime - startTime).total_seconds()

        # Update schedulableTime after the last run.
        self.schedulableTime = endTime + self.timeDelta
        print("[%s] Started: %s took %d seconds to run. (Returned: %s). Next run: %s" %
              (self.operation, startTime, elapsedSeconds, ret, self.schedulableTime))


    def run(self):
        startTime = datetime.datetime.now()
        #self.schedulableTime = startTime + self.timeDelta
        #print("Now: %s, Next run: %s" % (startTime.strftime("%Y-%m-%d %H:%M:%S"),
        #           self.schedulableTime.strftime("%Y-%m-%d %H:%M:%S")))
        jobThread = threading.Thread(target=self.threadedRun)
        jobThread.start()
        #ret = self.job_func()
        endTime = datetime.datetime.now()
        elapsedSeconds = (endTime - startTime).total_seconds()



def main():
    # User input.
    # Define a job:
    # Run every minute.
    scheduler = Scheduler()

    options = {
        'operation': "IAM_POLICY_CHECKER",
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
    scheduler.schedule_job(**options)

    options = {
        'operation': 'EC2_LOW_UTILIZATION',
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
    scheduler.schedule_job(**options)

    options = {
        'operation': 'EBS_VOLUMES_CHECK',
        'schedule': {
            'every': 1,
            'unit': 'minutes'
        },
        'jobFunction': test_job,
        'jobOptions': {
            'apikey': 'DKRlsk',
            'session': 'test'
        }
    } 
    scheduler.schedule_job(**options)

    for x in range(50):
        scheduler.run_pending()
        time.sleep(2)



if __name__ == '__main__':
    main()
