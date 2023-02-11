#!/bin/bash

# Simple script so we dont have to keep typing the same command all the time
# Copy this script to each folder, just change the parameters

# Change these values to match the stack.

STACK_NAME="teststack1"
TEMPLATE_BODY="file://teststack.yaml"
PARAMETERS_FILE="file://teststack_params.json"
PROFILE=" --profile dev --region us-east-1"
CAPABILITIES="--capabilities CAPABILITY_NAMED_IAM"



# Do not change.

if [[  -z $1 ]]; then
    echo "Need to specify one of [create, delete, update] as argument"
    exit 1
fi

if [[ $1 = "create" ]]; then
    echo "Create"
    set -x
    aws cloudformation create-stack --stack-name $STACK_NAME \
        --template-body $TEMPLATE_BODY --parameters $PARAMETERS_FILE \
        $PROFILE $CAPABILITIES

elif [[ $1 = "update" ]]; then
    echo "update"
    set -x
    aws cloudformation update-stack --stack-name $STACK_NAME \
        --template-body $TEMPLATE_BODY --parameters $PARAMETERS_FILE \
        $PROFILE $CAPABILITIES

elif [[ $1 = "delete" ]]; then
    echo "delete"
    set -x
    aws cloudformation delete-stack --stack-name $STACK_NAME $PROFILE

else
    echo "Need to specify one of [create, delete, update] as argument"
    exit 1
fi

