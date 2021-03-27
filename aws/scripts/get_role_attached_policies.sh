#!/bin/bash

profile=$1
PROFILE_OPTION=""

if [[ ! -z $profile ]]; then
    echo "PROFILE: $profile"
    PROFILE_OPTION="--profile $profile"
fi

roles=$(aws iam list-roles --output text $PROFILE_OPTION| grep ROLES | awk -F" " '{print $7}')
for role in $roles
do
    policy_count=$(aws iam list-attached-role-policies --role-name $role --output text $PROFILE_OPTION | grep ATTACHEDPOLICIES | wc -l)
    if [[ $policy_count -gt "8" ]]; then
        printf "%-40s : %10s \n" $role $policy_count 
    fi
done

