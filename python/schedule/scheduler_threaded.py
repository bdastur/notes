#!/usr/bin/env python                                                               
# -*- coding: utf-8 -*- 

'''
For jobs that take longer to run it is not recommended to run them
'''

import datetime
import threading
import time
import schedule


def check_password_policy():
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[%s] passwd policy check  %s" % (curTime, threading.current_thread()))
    time.sleep(3)
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[%s] passwd policy check complete %s" % (curTime, threading.current_thread()))


def check_iam_roles():
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[%s] IAM roles check %s" % (curTime, threading.current_thread()))
    for x in range(10000):
        pass
    time.sleep(7)
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[%s] IAM roles check complete %s" % (curTime, threading.current_thread()))


def check_trustedadvisor_limits():
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[%s] Checking TA limits %s" % (curTime, threading.current_thread()))
    time.sleep(20)
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[%s] Checking TA limits complete %s" % (curTime, threading.current_thread()))


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def main():
    schedule.every(10).seconds.do(run_threaded, check_iam_roles)

    for job in schedule.get_jobs():
        print("Job info: %s [%s]" % (job.job_func.args, job.next_run))

        
    count = 0
    for x in range(80):
        schedule.run_pending()
        time.sleep(2)
        print("Sleeping for 2 seconds")
        if count == 5:
            print("Add trusted advisor check to schedule")
            schedule.every(10).seconds.do(run_threaded, check_trustedadvisor_limits)

        if count == 9:
            print("Add check password policy")
            schedule.every(10).seconds.do(run_threaded, check_password_policy)


        if count % 6 == 0:
            print("-------------------------")
            for job in schedule.jobs:
                print("Job info: %s [%s] [%s]" %(job.job_func.args, job.last_run, job.next_run))
            print("-------------------------")
        count += 1


if __name__ == '__main__':
    main()
