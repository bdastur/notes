#!/bin/bash

operation=
image=${APP_DEFAULT_IMAGE}
deploymentconfigfile=

valid_operations=("build" "push" "deploy")

function usage {
    echo "Usage: app.sh <operation> [options]"
    echo "-----------------------------------"
    echo "Allowed Operations: ${valid_operations[@]}"
    echo "Examples: "
    echo ""
    echo "build a docker image:"
    echo "./app build ."
    echo "./app build -i registry.abc.acme.com/alpine:1.0"
    echo ""
    echo "deploy a oc template:"
    echo "./app deploy openshift/deploymentconfig.yaml"
    echo ""    
    
    exit 1
}

function validate_operation {
  #statements
  local operation=$1
  valid=false
  echo "operation: $operation"
  for x in ${valid_operations[@]}; do
    if [[ $x == "$operation" ]]; then
        valid=true
    fi
  done

  if [[ $valid == false ]]; then
    echo "Invalid operation $operation. Must be one of: '${valid_operations[@]}'"
    exit 1
  fi
}

function app_operation_build {
    local args=$1
    echo "image: $image, args: $args"
    docker build --tag=$image $args
}

function app_operation_deploy {
    echo "dep config: $deploymentconfigfile"
    formatimage=$(echo $image | sed 's/\//\\\//g')
    echo "sed  's/APP_DEFAULT_IMAGE/${formatimage}/' $deploymentconfigfile"
    cat $deploymentconfigfile | sed "s/APP_DEFAULT_IMAGE/${formatimage}/" > /tmp/tempdeployment.yaml
    oc process -f /tmp/tempdeployment.yaml | oc apply -f - 
}


# Simple helper script.
echo "print all $*"

if [[ $# -eq 0 || $1 == '-h' ]]; then
    usage
fi

echo "here"

readonly COMMANDLINE="$*"

#######################################
# Parse the positional arguments first.
# In this case it is the type of operation.
# Once we parse it 'shift' all the command line arguments
# one position to the left.
#######################################

# Get service type.
operation=$1
image=${APP_DEFAULT_IMAGE}

validate_operation $operation
shift

CMD_OPTIONS="i:f:"

while getopts ${CMD_OPTIONS} option; do
  case $option in
      f)
          deploymentconfigfile=$OPTARG
          ;;
      i)
          image=$OPTARG
          shift
          shift
          ;;
      :) echo "Error option needs argument";; 
      *) echo "Error: Invalid option";;
  esac       
done

echo "deployment config: $deploymentconfigfile"
echo "args remaining: $*"
app_operation_${operation} $*
