IMAGENAME ?= pyspark:latest
NAME ?= pyspark
build: Dockerfile
	finch build -t $(IMAGENAME) .

# The cache for RUN instructions in a Dockerfile do not get invalidated automatically.
# You can invalidate them by using --no-cache flag.

build-nocache: Dockerfile
	finch build --no-cache -t $(IMAGENAME) .

run-it:
	finch rm -f $(NAME)
	finch run --name $(NAME) -it $(IMAGENAME) /opt/spark/bin/pyspark

clean:
	finch rmi $(IMAGENAME) 


#finch run -it apache/spark-py /opt/spark/bin/pyspark
