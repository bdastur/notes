#!/bin/bash

#################################################################################
# Terraform Bootstrap.
# --------------------
# Allows you to specify a region to bootstrap.
#################################################################################

if [[ $# -eq 0 ]]; then
    echo "No arguments provided"
    exit
fi

while getopts b:r: flag
do
    case "${flag}" in
        b)
            echo "Chosen b ${OPTARG}";;
        r)
            echo "Chosed r ${OPTARG}";;
    esac
done

