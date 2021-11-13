#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A simple example of using schedule library.
'''

import datetime
import schedule
import time



def check_iam_password_policy():
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("Checking iam password policy: ", curTime)


def check_trustedadvisor_limits():
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("Check trusted advisor limits: ", curTime)
    time.sleep(8)



def main():
    # Set schedules.
    schedule.every(10).seconds.do(check_iam_password_policy)
    schedule.every(15).seconds.do(check_trustedadvisor_limits)

    for i in range(50):
        schedule.run_pending()
        time.sleep(2)
        print("Sleep for 2 seconds")
        print(schedule.jobs)

if __name__ == '__main__':
    main()
