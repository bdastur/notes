IMAGENAME ?= jsbuilder:latest
build: Dockerfile
	docker build -t $(IMAGENAME) .

# The cache for RUN instructions in a Dockerfile do not get invalidated automatically.
# You can invalidate them by using --no-cache flag.

build-nocache: Dockerfile
	docker build --no-cache -t $(IMAGENAME) .

run-it:
	docker rm -f base
	docker run --name base -p 1234:1234 -v ./projects:/projects -it $(IMAGENAME) /bin/bash

clean:
	docker rmi $(IMAGENAME) 
