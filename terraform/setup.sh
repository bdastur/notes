#!/bin/bash

###########################################################################
# TF Setupscript
# ---------------
# A simple utility to automate some of the pre-requisites and some manual steps to
# to make it easy to use these tools.
#
# Operations:
# -----------
#   bootstrap:
#   ---------
# Creates an S3 bucket, that will be used to manage Terraform state.
# Terraform manages state for the resources it creates as a .tfstate file that is
# by default created locally, but with the S3 backend it manages state on S3.
#
#  clone_template:
#  --------------
# Copy a specific terraform folder eg: MysqlInstance, to a deploymenet
# folder.
#
###########################################################################

source ./scripts/validationFunctions.sh

accountId=
bucketPrefix="tfstate"


function showUsageHelp() {
    echo "--------------------------------------------------"
    echo "setup.sh: Setup script to make it easier to work with the tf templates"
    echo "Usage: setup.sh <operation> [options]"
    echo "Supported operations: bootstrap|destroy|list-templates|clone-template"
    echo "  bootstrap: Run once for specific account to setup TF S3 Bucket"
    echo "  destroy: Run to delete the terraform s3 bucket"
    echo "  list-templates: List available terraform templates"
    echo "  clone-template: Copy a template to staging dir, for deployment"
    echo ""
    echo "Example command executions: "
    echo "  bootstrap: ./setup.sh bootstrap -r us-east-1 -p dev"
    echo "  destroy: ./setup.sh bootstrap -r us-east-1 -p dev"
    echo "  list-templates: ./setup.sh list-templates"
    echo "  clone-template: ./setup.sh clone-template -r us-east-1 -p dev -t MySQLInstance"
    echo ""
    echo "Options: "
    echo "  -r: Region   [help: Region name.                                   Usage -r us-east-1]"
    echo "  -p: Profile  [help: profile name as present in ~/.aws/credentials. Usage -p default]"
    echo "  -t: Template [help: TFTempalte folder to clone.                    Usage -t MySQLInstance]"
    echo "--------------------------------------------------"
    exit 1
}

function getAccountId() {
    local profile=$1
    local region=$2
    id=$(aws sts get-caller-identity --output text --profile $profile --region $region | awk -F" " '{print $1}')
    if [[ -z $id ]]; then
        echo "could not get Account ID."
        showUsageHelp
    fi
    accountId=$id
}

function getTFBucketName() {
    local profile=$1
    local region=$2
    getAccountId $profile $region
    echo "$bucketPrefix-$accountId-bucket"
}

function bootstrapTerraform() {
    local profile=$1
    local region=$2
    getAccountId $profile $region
    echo "Account id: $accountId"
    bucketName=$(getTFBucketName $profile $region)
    bucket=$(getTerraformBucket $profile $region $bucketName)
    if [[ -z $bucket ]]; then
        echo ""
        read -p "You are about to create $bucketName in $accountId. Sure? [y/n]: " option

        if [[ $option != "y" ]]; then
            echo "Skip creating bucket $bucketName"
            exit 0
        fi
        # Create bucket (We will default create in us-east-1 (no specific reason to
        # create it in any other region.
        output=$(aws s3api create-bucket --bucket $bucketName --profile $profile --region us-east-1)
        if [[ $? -ne 0 ]]; then
            echo "Bucket ($bucketName) creation failed"
            exit 1
        fi
    else
        echo "Bucket $bucketName exists.. Do nothing"
    fi

}

function destroy() {
    local profile=$1
    local region=$2
    getAccountId $profile $region
    bucketName="$bucketPrefix-$accountId-bucket"
    bucket=$(getTerraformBucket $profile $region $bucketName)
    if [[ -z $bucket ]]; then
        echo "Bucket $bucketName not found. Exit"
        exit 1
    fi

    echo ""
    read -p "You are about to delete $bucketName in $accountId. Sure? [y/n]: " option

    if [[ $option != "y" ]]; then
        echo "Skip deleting $bucketName"
        exit 0
    fi

    echo "Destroying bucket $bucketName in $accountId"
    output=$(aws s3api delete-bucket --bucket $bucketName --profile $profile)
    if [[ $? -ne 0 ]]; then
        echo "Bucket deletion for $bucketName failed"
         exit $?
    else
        echo "Bucket $bucketName deleted!"
    fi

}

function getTerraformBucket() {
    local profile=$1
    local region=$2
    local bucketName=$3

    bucket=$(aws s3api get-bucket-location --bucket $bucketName --profile $profile)
    echo $bucket
}

function listTemplates() {
    local templatePath="tfTemplates"

    templates=$(ls -1 $templatePath)
    for template in ${templates[*]}; do
        echo "---------------------------------------"
        echo "Template: $template"
        descriptionFile="$templatePath/$template/description.txt"
        if [[ -f $descriptionFile ]]; then
            cat $templatePath/$template/description.txt
        else
            echo "No description set"
        fi
    done
    echo "---------------------------------------"
}

function cloneTemplate() {
    local profile=$1
    local region=$2
    local templateName=$3

    local bucketName=$(getTFBucketName $profile $region)
    if [[ -z $bucketName ]]; then
        echo "Could not get BucketName"
        exit 1
    fi
    bucket=$(getTerraformBucket $profile $region $bucketName)
    if [[ -z $bucket ]]; then
        echo "TF Bucket $bucketName does not exist. Bootstrap first!"
        exit 1
    fi

    local templatePath="tfTemplates"
    templateDir="$templatePath/$templateName"
    if [[ ! -d $templateDir ]]; then
        echo "Invalid template name $templateName"
        exit 1
    fi

    getAccountId $profile $region
    echo "Account id: $accountId"

    stageDir="envStage"
    tfFolder="${templateName}_${region}_${accountId}"
    echo "TFFolder: $tfFolder"
    if [[ -d $stageDir/$tfFolder ]]; then
        echo "Folder: $stageDir/$tfFolder exists. Skip creation."
        echo "Delete the staging folder $stageDir/$tfFolder, if you want to re-create"
        exit 1
    fi

    output=$(mkdir $stageDir/$tfFolder)
    if [[ $? -ne 0 ]]; then
        echo "Failed to create $stageDir/$tfFolder"
        exit 1
    fi

    # Copy all files from
    cp $templateDir/*tf $stageDir/$tfFolder/.
    if [[ $? -ne 0 ]]; then
        echo "Failed to copy templates"
        exit 1
    fi

    cp $templateDir/*.json $stageDir/$tfFolder/.
    if [[ $? -ne 0 ]]; then
        echo "Failed to copy templates"
        exit 1
    fi

    if [[ -d $templateDir/user_data ]]; then
        cp -R $templateDir/user_data $stageDir/$tfFolder/.
        if [[ $? -ne 0 ]]; then
            echo "Failed to copy templates"
            exit 1
        fi
    fi
    # Update template variables.
    sed -i -e "s/REGION_REPLACE/$region/g" $stageDir/$tfFolder/*.tf $stageDir/$tfFolder/*.json
    sed -i -e "s/PROFILE_REPLACE/$profile/g" $stageDir/$tfFolder/*.tf $stageDir/$tfFolder/*.json
    sed -i -e "s/BUCKET_NAME_REPLACE/$bucketName/g" $stageDir/$tfFolder/*.tf $stageDir/$tfFolder/*.json

    # Cleanup unwanted files.
    rm $stageDir/$tfFolder/*.tf-e $stageDir/$tfFolder/*.json-e

}

#----------------------------------------------------------------------
# Main Script starts here.
#----------------------------------------------------------------------

readonly COMMANDLINE="$*"

# Validate Prerequisites as the first step. At each validation stage, if we fail,
# we will exit the script.
validatePrerequisites

operation=$1
if [[ -z $operation || $operation == "-h" ]]; then
    showUsageHelp
fi

validateOperation $operation
shift

CMD_OPTIONS="p:r:t:h"

while getopts ${CMD_OPTIONS} option; do
    case $option in
        h)
            showUsageHelp
            ;;
        p)
            profile=$OPTARG
            ;;
        r)
            region=$OPTARG
            ;;
        t)
            template=$OPTARG
            ;;
        :) echo "Error: option \"-$OPTARG\" needs argument";;
        *) echo "Error: Invalid option \"-$OPTARG\"";;
    esac
done

# Execute Operation.
if [[ $operation == "bootstrap" ]]; then
    bootstrapTerraform $profile $region
elif [[ $operation == "destroy" ]]; then
    destroy $profile $region
elif [[ $operation == "list-templates" ]]; then
    listTemplates
elif [[ $operation == "clone-template" ]]; then
    cloneTemplate $profile $region $template
fi




