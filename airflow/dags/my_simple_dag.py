#!/usr/bin/env python
# -*- coding: utf-8 -*-    

import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def greet():
    print('Writing in file')
    with open('path/to/file/greet.txt', 'a+', encoding='utf8') as f:
        now = dt.datetime.now()
        t = now.strftime("%Y-%m-%d %H:%M")
        f.write(str(t) + '\n')
    return 'Greeted'
def respond():
    return 'Greet Responded Again'
