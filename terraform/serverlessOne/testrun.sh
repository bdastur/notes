#!/bin/bash

echo "Test execution start.."

cat > payload.json << EOL
{
  "Key": "Value",
  "path": "This is a test path from cli"
}
EOL

aws lambda invoke \
    --function-name lambda_function_one \
    --output json --payload file://payload.json \
    --cli-binary-format raw-in-base64-out  \
    --profile dev \
    --region us-east-1  output.json

echo "Output: "
cat output.json | jq

rm payload.json output.json
