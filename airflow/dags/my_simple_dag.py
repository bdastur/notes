#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago


def greet():
    print('Writing in file')
    with open('/tmp/greet.txt', 'a+') as f:
        now = dt.datetime.now()
        msg = "Greet : %s" % str(now.strftime("%Y-%m-%d %H:%M:%S"))
        t = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(msg + '\n')
    return 'Greeted'

def respond():
    print('Respond Writing in file')
    with open('/tmp/greet.txt', 'a+') as f:
        now = dt.datetime.now()
        msg = "Respond : %s" % str(now.strftime("%Y-%m-%d %H:%M:%S"))
        t = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(msg + '\n')
    return "Respond"

def argue():
    print('Writing in file')
    with open('/tmp/greet.txt', 'a+') as f:
        now = dt.datetime.now()
        msg = "Argue : %s" % str(now.strftime("%Y-%m-%d %H:%M:%S"))
        t = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(msg + '\n')
    return 'argue'

default_args = {
    'owner': 'behzad.dastur',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1)
}

dag = DAG(
    "mysimpledag",
    description="This is a simple example of bash and python operator",
    schedule_interval=dt.timedelta(seconds=20),
    default_args=default_args
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date >> /tmp/greet.txt',
    dag=dag,
)

t2 = PythonOperator(
    task_id="Greet",
    python_callable=greet,
    dag=dag
)

t3 = PythonOperator(
    task_id="Respond",
    python_callable=respond,
    dag=dag
)

t4 = PythonOperator(
    task_id="Argue",
    python_callable=argue,
    dag=dag
)


t1 >> [t2, t3] >> t4
