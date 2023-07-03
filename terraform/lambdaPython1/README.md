# Lambda Python Example.

* In this example, we have a python lambda function that is triggered by a cloudwatch
eventbridge schedule timer at a rate of x minutes.
* The lambda function simply calls s3 list buckets and returns a json output
  if successful.
* There is also a cloudwatch log group created explicitly with a retention time of
  x days, and permissions added for lambda to send cw logs.
* A SNS topic is created and configured for lambda function to push message to the
  topic in case of falure.


                           |cw logs|
                            ^
                            |
|cloudwatch timer| ----> |Lambda function| --------------> |SNS Topic|
                            |                (on failure)
                            v
                      (s3 list buckets)


