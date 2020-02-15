# Airflow

*Links:*
[Airflow Project](https://airflow.apache.org/docs/stable/project.html)


Airflow is a tool for describing, executing and monitoring workflows


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

