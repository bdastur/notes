imageName = examples/simpleserver
imageVersion ?= latest
profile ?= dev
region ?= us-east-1
valuesFile =
account =
ecrRepository = $(account).dkr.ecr.$(region).amazonaws.com

build: Dockerfile src/*
	test -n "$(account)" #check if account-id is passed
	aws ecr get-login-password --region us-east-1 --profile $(profile) | finch login --username AWS --password-stdin $(ecrRepository)
	finch build --platform linux/amd64  --tag $(imageName) .
	finch tag $(imageName):latest $(ecrRepository)/$(imageName):$(imageVersion)
	finch push $(ecrRepository)/$(imageName):$(imageVersion)

