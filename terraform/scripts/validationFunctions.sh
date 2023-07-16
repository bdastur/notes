#!/bin/bash

#----------------------------------------------------------------------
# Validation functions
#----------------------------------------------------------------------
validPrerequisites=("terraform" "aws")
validOperations=("bootstrap" "destroy" "list-templates" "clone-template")
validRegions=("us-east-1", "us-east-2", "us-west-1", "us-west-2")

successIcon="\xE2\x9C\x94"
failureIcon="\xE2\x9D\x8C"


function validatePrerequisites() {
    echo "Validating pre-requisites.."
    validated="true"
    for prereq in ${validPrerequisites[*]}; do
        test=$(which $prereq)
        if [[ -z $test ]]; then
            echo -e " * $prereq: failed validation $failureIcon"
            validated="false"
        else
            echo -e " * $prereq: validated $successIcon"
        fi
        sleep 0.6
    done

    if [[ $validated == "false" ]]; then
        echo "Pre-Requisites not met! Please fix and rerun"
        exit 1
    fi
}

function validateOperation() {
    local operation=$1
    validated="false"

    for validOper in ${validOperations[*]}; do
        if [[ $validOper == $operation ]]; then
            validated="true"
        fi
    done

    if [[ $validated == "false" ]]; then
        echo "Operation $operation is not valid"
        showUsageHelp
        exit 1
    fi
}

