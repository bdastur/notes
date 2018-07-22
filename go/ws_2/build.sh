#!/bin/bash

export GOPATH=$(pwd)

# Get required packages.
go get gopkg.in/yaml.v2
go get -u github.com/aws/aws-sdk-go
make
