CURRENT_PATH := $(shell pwd)

build: Dockerfile
	docker build --tag airflow:0.1 .

clean:
	docker rm -f airflow

test:
	docker run -it --name airflow \
		--cpus="0.5" \
		--memory="0.5g" \
		-p 8080:8080 \
		-v ${CURRENT_PATH}/dags:/root/airflow/dags \
		airflow:0.1 bash

