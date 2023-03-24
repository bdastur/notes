#!/bin/bash

#################################################################################
# Terraform Bootstrap.
# --------------------
# Allows you to specify a region to bootstrap.
#################################################################################

TFBucketNamePrefix="cwbench-terraform-state"
TFBucketName=""
profile=""
region=""


function validateRegions() {
    validRegions="us-east-1 us-east-2 us-west-1 us-west-2 af-south-1 ap-east-1 ap-northeast-1 ap-northeast-2 ap-northeast-3 ap-south-1 ap-southeast-1 ap-sourheast-2 ca-central-1 cn-north-1 cn-northwest-1 eu-central-1 eu-north-1 eu-south-1 eu-west-1 eu-west-2 eu-west-3 me-south-1 sa-east-1 us-gov-east-1 us-gov-west-1"

    local region=$1

    for r in ${validRegions[@]}; do
        if [[ $region == $r ]]; then
            validRegion="true"
        fi
    done

    if [[ $validRegion != "true" ]]; then
        echo "Region invalid. Must be one of: $validRegions"
        exit 1
    fi
}

function validateOperation() {
    validOperations="list init destroy"
    operation=$1

    for oper in ${validOperations[@]}; do
        if [[ $operation == $oper ]]; then
            validOperation="true"
            break
        fi
    done

    if [[ $validOperation != "true" ]]; then
        echo "Operation must be one of: $validOperations"
        exit 1
    fi
}

function validateListOperation() {
    local profile=$1
    local region=$2

    validateRegions $region

    if [[ -z $profile ]]; then
        echo "$profile in -z"
    fi

    BucketNameStr=$(setBucketName $TFBucketNamePrefix $region)

    # List S3 buckets.
    data=$(aws s3api list-buckets --profile $profile --output text)
    if [[ $? -ne 0 ]]; then
        echo "Error: List buckets failure."
        exit $?
    fi
}


function listOperation() {
    local profile=$1
    local region=$2
    validateListOperation $profile $region

    buckets=($(aws s3api list-buckets --profile $profile --output text| awk -F" " '{print $3}'| grep $TFBucketNamePrefix))
    echo "Terraform State Backends (S3 Buckets)"
    echo "---------------------------------------"
    for bucket in ${buckets[@]}; do
        echo "Bucket: $bucket"
        bucketFound="true"
    done

    if [[ $bucketFound != "true" ]]; then
        echo "  No Terraform state buckets found.."
    fi
    echo ""
}


function initOperation() {
    local profile=$1
    local region=$2

    bucketNameStr=$(setBucketName $TFBucketNamePrefix $region)
    echo "Bucket to create: $bucketNameStr"

    # Check if bucket name already exists.
    bucket=$(aws s3api list-buckets --profile $profile --output text| awk -F" " '{print $3}'| grep $bucketNameStr)
    if [[ $? -eq 0 ]]; then
        echo "Terraform state Bucket \"$bucket\" already exists.."
        exit 1
    fi

    #Create a new bucket.
    locationConstraintOption=""
    if [[ $region != "us-east-1" ]]; then
        locationConstraintOption="--create-bucket-configuration LocationConstraint=$region"
    fi

    createCmd="aws s3api create-bucket --bucket $bucketNameStr $locationConstraintOption --profile $profile --region $region"
    echo "CMD: $createCmd"

    output=$($createCmd)
    if [[ $? -ne 0 ]]; then
        echo "Bucket creation failed.."
        exit 1
    fi
}

function destroyOperation() {
    local profile=$1
    local region=$2

    bucketNameStr=$(setBucketName $TFBucketNamePrefix $region)
    echo "Bucket to destroy: $bucketNameStr"

    # Check if bucket exists.
    bucket=$(aws s3api list-buckets --profile $profile --output text| awk -F" " '{print $3}'| grep $bucketNameStr)
    if [[ $? -ne 0 ]]; then
        echo "Terraform state Bucket \"$bucketNameStr\" does exists.."
        exit 1
    fi

    # Destroy the bucket.
    deleteCmd="aws s3api delete-bucket --bucket $bucketNameStr --profile $profile"
    echo "CMD: $deleteCmd"

    read -p "Are you sure you want to destroy the bucket [y/n]: " option
    if [[ $option == "y" ]]; then
        output=$($deleteCmd)
        if [[ $? -ne 0 ]]; then
            echo "Bucket deletion for bucket $bucketNameStr failed"
            exit $?
        else
            echo "Bucket $bucketNameStr successfully deleted"
            exit 0
        fi
    else
        echo "Skipped deleting bucket $bucketNameStr"
    fi

}


function showHelp() {
    echo "`basename $0`  : Terraform Bootstrap"
    echo "-------------------------------------------------"
    echo "usage: bootstrap_tf.sh [operation] [options]"
    echo ""
    echo "Available Operations: "
    echo "---------------------"
    echo " init: Initialize/bootstrap terraform state S3 bucket"
    echo " destroy: destroy a terraform state S3 bucket"
    exit 1

}


###############################
# Get current terraform state buckets.
###############################
function getTFStateBuckets() {
    local profile=$1
    local region=$2
}

function setBucketName() {
    local namePrefix=$1
    local region=$2
    local nameSuffix=$3
    TFBucketName="${namePrefix}-${region}"
    echo $TFBucketName
}



if [[ $# -eq 0 || $1 = "-h" ]]; then
    echo "No arguments provided"
    showHelp
fi

########################################
# Once we read the positional argument
# we shift all the command line arguments
# one position to the left.
########################################
operation=$1
shift

validateOperation $operation

CMD_OPTIONS="b:hp:r:"

while getopts ${CMD_OPTIONS} option; do
    case "${option}" in
        p)
            profile=${OPTARG}
            ;;
        r)
            region=${OPTARG}
            ;;
        :)
            echo "Invalid optional arguments";;
        *)
            echo "Invalid optional arguments";;
    esac
done

# Need to validate required options.
# We need to check if options are set before any other validations.
if [[ -z $profile ]]; then
    echo "Error: Missing required option -p (profile)"
    exit 1
fi

if [[ -z $region ]]; then
    echo "Error: Missing required option -r (region)"
    exit 1
fi


# List operation.
if [[ $operation == "list" ]]; then
    listOperation $profile $region
fi


# init operation.
if [[ $operation == "init" ]]; then
    initOperation $profile $region
fi

# destroy operation.
if [[ $operation == "destroy" ]]; then
    destroyOperation $profile $region
fi


