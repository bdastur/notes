#!/bin/bash


export AIRFLOW_HOME=/airflow
airflow initdb
airflow webserver -p 8080 &

airflow scheduler

