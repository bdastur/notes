####################################
# Make
# How to build?
# -------------
#  make region=us-east-1 account=<account id> build
#
# What does it do?
# ---------------
#  Connect to ECR, build and tag the image and push it to the ECR repository.
#
#  Prerequisites:
#  --------------
#  You will need to have access to AWS Account. Create a ECR repository
#  <namespace>/<Repo> = examples/samplepy, grant permissions to push, pull from
#  the repo.
#
# Example:
# make account=xxxxxx build
# make valuesFile=/tmp/dev_values.yaml helm-install
# make valuesFile=/tmp/dev_values.yaml helm-upgrade
#
###################################
helmAppName = simpleapps
imageName = examples/samplepy
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

helm-install:
	test -n "$(valuesFile)" # Check if repository is passed. 
	helm install $(helmAppName) helmcharts/$(helmAppName)/ --values helmcharts/$(helmAppName)/values.yaml -f $(valuesFile)

helm-upgrade:
	test -n "$(valuesFile)" # Specify a values yaml file.
	helm upgrade $(helmAppName) ./helmcharts/$(helmAppName) -f $(valuesFile)

helm-uninstall:
	helm uninstall $(helmAppName)


check-env:
	ifndef $(account)
		$(error account is undefined)
	endif
