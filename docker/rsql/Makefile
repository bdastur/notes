imagename = rsql:latest
name = rsql
build: Dockerfile
	finch build --platform linux/x86_64 -t $(imagename) .

# The cache for RUN instructions in a Dockerfile do not get invalidated automatically.
# You can invalidate them by using --no-cache flag.

build-nocache: Dockerfile
	finch build --no-cache --platform linux/x86_64 -t $(imagename) .

run-it:
	finch rm -f $(name)
	finch run --name $(name) -it $(imagename) /bin/bash

clean:
	finch rmi $(imagename) 
