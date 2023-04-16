#!/bin/bash

lambdaFunction=$1
profile=$2
region=$3

echo "Lambda function: $lambdaFunction"

if [[ -z $lambdaFunction ]]; then
    echo "Usage: testrun.sh <lambda function name>"
    exit 1
fi

if [[ -z $profile ]]; then
    echo "No profile set, default to 'dev'"
    profile=dev
fi

if [[ -z $region ]]; then
    echo "No region set, default to 'us-east-1'"
    region="us-east-1"
fi


echo "Test execution start.."

cat > payload.json << EOL
{
  "Key": "Value",
  "path": "This is a test path from cli"
}
EOL

aws lambda invoke \
    --function-name $lambdaFunction \
    --output json --payload file://payload.json \
    --cli-binary-format raw-in-base64-out  \
    --profile $profile \
    --region $region  output.json

echo "Output: "
cat output.json | jq

rm payload.json output.json


