imagename = githelper:latest
build: Dockerfile
	docker build -t $(imagename) .

# The cache for RUN instructions in a Dockerfile do not get invalidated automatically.
# You can invalidate them by using --no-cache flag.

build-nocache: Dockerfile
	docker build --no-cache -t $(imagename):latest .

run-it:
	docker rm -f base
	docker run --name base -it $(imagename) /bin/bash

clean:
	docker rmi $(imagename)

