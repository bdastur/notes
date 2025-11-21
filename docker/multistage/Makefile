IMAGENAME ?= gobuild:latest
build: Dockerfile
	docker build -t $(IMAGENAME) .

# The cache for RUN instructions in a Dockerfile do not get invalidated automatically.
# You can invalidate them by using --no-cache flag.

build-nocache: Dockerfile
	docker build --no-cache -t $(IMAGENAME) .

build-debug: Dockerfile
	docker build --no-cache -t $(IMAGENAME) --progress=plain .

scan-trivy: Dockerfile
	docker run aquasec/trivy image ${IMAGENAME} 

lint: Dockerfile
	hadolint Dockerfile

run:
	docker run ${IMAGENAME}

run-it:
	docker rm -f base
	docker run --name base -v ./projects:/projects -it $(IMAGENAME) /bin/bash

clean:
	docker rmi $(IMAGENAME) 
