#!/bin/bash

profile="dev"
region="us-east-1"
operation=
name=
accountId=


#---------------------------------------------------
# Show Usage and Help function.
#---------------------------------------------------
function showUsageHelp() {
    echo ""
    echo "--------------------------------------------------"
    echo "Usage ./run_operation.sh <operation> -p <profile> -r <region> [-f <file>] [-n <state machine name>]"
    echo "Valid operations: create|delete|execute|describe-execution"
    echo ""
    echo "-----"
    echo "Examples: "
    echo "1. Create new state machine"
    echo "./run_operations.sh create -p dev -r us-east-1 -f file://first.asl.json"
    echo ""
    echo "2. Delete state machine"
    echo "./run_operations.sh delete -p dev -r us-east-1 -n first"
    echo ""
    echo "3. Execute state machine"
    echo "./run_operations.sh execute -p dev -r us-east-1 -e first-cli-execution -n first [-i <input json>]"
    echo ""
    echo "4. Describe Execution"
    echo "./run_operations.sh describe-execution -p dev -r us-east-1 -e first-cli-execution -n first"
    echo ""
    echo "--------------------------------------------------"
}

#---------------------------------------------------
# Validate operation
#---------------------------------------------------
validOperations=("create" "delete" "execute" "describe-execution")
function validateOperation() {
    local operation=$1
    validated="false"
    for validOperation in ${validOperations[*]}; do
        if [[ $validOperation == $operation ]]; then
            validated="true"
            break
        fi
    done

    if [[ $validated == "false" ]]; then
        echo "Operation $operation is not valid"
        showUsageHelp
        exit 1
    fi
}

#---------------------------------------------------
# Get AccountId from profile
#---------------------------------------------------
function getAccountId() {
    local profile=$1
    accountId=$(aws sts get-caller-identity --profile $profile --output text | awk -F" " '{print $1}')
    if [[ -z $accountId ]]; then
        echo "AccountId could not be retrieved"
        exit 1
    fi
}

#---------------------------------------------------
# Create Step function.
#---------------------------------------------------
function createStateMachine() {
    local profile=$1
    local region=$2
    local fileName=$3

    local stateMachineRoleName="StepFunctions-MyStateMachine-4fiwcr036-role-ba9wkwbla"

    echo "$fileName"
    stepFunctionName=$(echo $fileName | awk -F "file://" '{print $2}'| awk -F ".asl.json" '{print $1}')
    echo "Step function name: $stepFunctionName"

    # Create new step function.
    aws stepfunctions create-state-machine \
    --name $stepFunctionName --definition $fileName \
    --role-arn arn:aws:iam::${accountId}:role/service-role/${stateMachineRoleName} \
    --profile $profile --region $region
}

#---------------------------------------------------
# Delete Step function.
#---------------------------------------------------
function deleteStateMachine() {
    local profile=$1
    local region=$2
    local name=$3

    aws stepfunctions delete-state-machine \
  --state-machine-arn arn:aws:states:${region}:${accountId}:stateMachine:${name} \
  --profile $profile --region $region
}

#---------------------------------------------------
# Execute Step function.
#---------------------------------------------------
function executeStateMachine() {
    local profile=$1
    local region=$2
    local name=$3
    local executionName=$4
    local inputFile=$5
    local inputParam=

    if [[ ! -z $inputFile ]]; then
        inputParam="--input $inputFile"
    fi

    aws stepfunctions start-execution \
    --state-machine-arn arn:aws:states:${region}:${accountId}:stateMachine:${name} \
    --name ${executionName} \
    $inputParam \
    --profile ${profile} --region ${region}
}

#---------------------------------------------------
# Describe Execution of a Step function.
#---------------------------------------------------
function describeExecutionOfStateMachine() {
    local profile=$1
    local region=$2
    local name=$3
    local executionName=$4

    aws stepfunctions describe-execution \
    --execution-arn arn:aws:states:${region}:${accountId}:execution:${name}:${executionName} \
    --profile ${profile} --region ${region}

}


#---------------------------------------------------
# MAIN.
#---------------------------------------------------
readonly COMMANDLINE="$*"

operation=$1

if [[ -z $operation || $operation == "-h" ]]; then
    showUsageHelp
    exit 0
fi

echo "Operation: $operation"
validateOperation $operation
shift


CMD_OPTIONS="e:i:n:p:r:f:h"

while getopts ${CMD_OPTIONS} option; do
    case $option in
        h)
            showUsageHelp
            ;;
        e)
            executionName=$OPTARG
            echo "Setting execution name: $executionName"
            ;;
        i)
            inputFile=$OPTARG
            echo "Setting input file: $inputFile"
            ;;
        n)
            name=$OPTARG
            echo "Setting State machine name: $name"
            ;;
        p)
            profile=$OPTARG
            echo "setting profile $profile"
            ;;
        r)
            region=$OPTARG
            echo "setting region $region"
            ;;
        f)
            definitionFile=$OPTARG
            echo "setting definition file $file"
            ;;
        :)  echo "Error option \"--$OPTARG\" needs assignment";;
        *) echo "Error: Invalid option \"$OPTARG\"";;
    esac
done

echo "profile: $profile"
getAccountId $profile
echo "Account id found: $accountId"


if [[ $operation == "create" ]]; then
    createStateMachine $profile $region $definitionFile
    exit 0
fi

if [[ $operation == "delete" ]]; then
    deleteStateMachine $profile $region $name
fi

if [[ $operation == "execute" ]]; then
    executeStateMachine $profile $region $name $executionName $inputFile
fi

if [[ $operation == "describe-execution" ]]; then
    describeExecutionOfStateMachine $profile $region $name $executionName
fi



