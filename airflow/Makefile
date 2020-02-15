CURRENT_PATH := $(shell pwd)

build: Dockerfile
	docker build --tag airflow:0.1 .

clean:
	docker rm -f airflow

test:
	docker run -it --name airflow \
		-p 8080:8080 \
		-v ${CURRENT_PATH}/dags:/airflow/dags \
		airflow:0.1 bash

