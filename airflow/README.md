# Airflow

Airflow is a tool for describing, executing and monitoring workflows            

*Links:*
* [Airflow Project](https://airflow.apache.org/docs/stable/project.html)
* [Developing workflows with Airflow](http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/)
* [Stackoverflow - airflow mysql connection](https://stackoverflow.com/questions/50632598/running-airflow-tasks-in-parallel-nothing-gets-scheduled)
* [Airflow db init fails with mysql](https://stackoverflow.com/questions/55223423/airflow-fail-to-initialize-db)



## Concepts:

### DAG:
Directed Acyclic Graph - it is a collection of all the tasks you want to run,
organized in a way that reflects their relationships and dependencies.

* A DAG is defined in a python script, which represents the DAGs structure.
* Not concerned with what the tasks do, but to sure they happen at the right
  time in the right order or with right handling of any unexpected  issues.
* DAGs should be placed in Airflow's DAG_FOLDER.



#### DAG Runs:
* Physical instance of a DAG, containing task instances that run for a
  specific execution_date.

* A DAG run is created by the airflow scheduler, but can also be created by an
  external trigger. Multiple DAG runs may be running at once for a particular
  DAG, each of them having a different execution_date.

##### execution_date:
* A logical date and time which the DAG Run and it's task instances are 
  running for.
* This allows task instances to process data for the desired logical date
  and time.



## Commands:

Unpause a DAG:

```
docker exec -t airflow /usr/bin/airflow unpause mysimpledag
```

Trigger a DAG Run:

```
$ docker exec -t airflow /usr/bin/airflow trigger_dag mysimpledag
```
