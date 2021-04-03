#!/bin/bash

set -xe

aws iam create-user --path /operations/ --user-name test1 --profile cloudops

