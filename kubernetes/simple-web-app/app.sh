#!/bin/bash

operation=
valid_operations=("build" "push")

function usage {
    echo "Usage: app.sh <operation> [options]"
    echo "-----------------------------------"
    exit 1
}

function validate_operation {
  #statements
  local operation=$1
  echo "operation: $operation"
  for x in ${valid_operations[@]}; do
    echo "$x"
  done
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
validate_operation $operation
shift


