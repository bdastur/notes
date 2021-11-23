#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
For jobs that take longer to run it is not recommended to run them
'''

import datetime
import threading
import time
import schedule


def check_password_policy(**kwargs):
    startTime = datetime.datetime.now()
    print("[%s] passwd policy check  %s" % (startTime, threading.current_thread()))
    time.sleep(3)
    endTime = datetime.datetime.now()
    diff = endTime - startTime
    print("check password policy took: %d" % (diff.total_seconds()))


def check_iam_roles(**kwargs):
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[%s] IAM roles check %s" % (curTime, threading.current_thread()))
    for x in range(10000):
        pass
    time.sleep(7)
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[%s] IAM roles check complete %s" % (curTime, threading.current_thread()))


def check_trustedadvisor_limits(**kwargs):
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[%s] Checking TA limits %s" % (curTime, threading.current_thread()))
    time.sleep(20)
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[%s] Checking TA limits complete %s" % (curTime, threading.current_thread()))

def wrapper_function(jobFunction, **kwargs):
    startTime = datetime.datetime.now()
    print("Wrapper start")
    jobFunction(**kwargs)
    print("Wrapper end")
    endTime = datetime.datetime.now()
    elapsedSeconds = (endTime - startTime).total_seconds()
    print("Thread %s elapsed time: %d" % (jobFunction, elapsedSeconds))


def run_threaded(job_func):
    print("Run threaded --> start")
    options = {
            "abckey": "value"
    }
    job_thread = threading.Thread(target=wrapper_function, args=[job_func], kwargs=options)
    job_thread.start()
    print("Run threaded --> End")


def main():
    schedule.every(10).seconds.do(run_threaded, check_iam_roles)
    schedule.every(15).seconds.do(run_threaded, check_trustedadvisor_limits)
    schedule.every(20).seconds.do(run_threaded, check_password_policy)

    print("-------------------------------")
    for job in schedule.get_jobs():
        print("Job info: %s [%s] [%s]" %(job.job_func.args, job.last_run, job.next_run))
    print("-------------------------------")

    count = 0
    for x in range(80):
        schedule.run_pending()
        time.sleep(2)

        #if count == 5:
        #    print("Add trusted advisor check to schedule")
        #    schedule.every(10).seconds.do(run_threaded, check_trustedadvisor_limits)

        #if count == 9:
        #    print("Add check password policy")
        #    schedule.every(10).seconds.do(run_threaded, check_password_policy)


        #if count % 8 == 0:
        #    print("-------------------------")
        #    for job in schedule.jobs:
        #        print("Job info: %s [%s] [%s]" %(job.job_func.args, job.last_run, job.next_run))
        #    print("-------------------------")
        #count += 1


if __name__ == '__main__':
    main()
