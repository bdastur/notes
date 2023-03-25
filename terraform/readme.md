# Terraform


## Links
* [Variables](https://www.terraform.io/docs/configuration/variables.html)
* [Infra cost - Get cost estimates for terraform projects](https://github.com/infracost/infracost)
* [Terratest - terraform testing framework](https://terratest.gruntwork.io/docs/getting-started/quick-start/)
* [Static analysis of terraform templates to spot security issues](https://github.com/aquasecurity/tfsec)
* [Collection of git hooks for Terraform](https://github.com/antonbabenko/pre-commit-terraform)
* [Terraform version manager](https://github.com/tfutils/tfenv)
* [Mineiros - github repo with collection of terraform utilities](https://github.com/mineiros-io)

## Variables:
* Terraform automatically loads any variable definition files if they are
  present:
  - Files named exactly terraform.tfvars or terraform.tfvars.json
  - Files with format\*.auto.tfvars or \*.auto.tfvars.json


* Terraform loads variables in following order, with latter sources taking
  precedence over earlier ones:
  - Environment variables
  - terraform.tfvars file if present
  - terraform.tfvars.json file if present
  - Any \*.auto.tfvars or \*.tfvars.json file - processed in lexical order of their filenames
  - Any -var and -var-file options on the commandline.

For example if I have a tfvars.json file that defines:
```
# more common.auto.tfvars.json
{
    "region": "us-west-2",
    "profile": "dev1"
}

```

and also set env variable:
```
$ export TF_VAR_region="us-east-1"

```

Terraform will pick the value of "us-west-2" for region
```
provider "aws" {
  region                  = var.region
  shared_credentials_file = var.credentials_file
  profile                 = var.profile
}
```


## Using tfsec:

### Docker option
```
~> docker pull aquasec/tfsec

~> <cd to source directory (.tf files) directory>
~> docker run --rm -it -v "$(pwd):/src" cde1d83bacab  /src

  Result 1

  [aws-lambda-enable-tracing][LOW] Resource 'aws_lambda_function.hello_example' uses default value for tracing_config.mode
  /src/main.tf:45-61


      42 | }
      43 |
      44 |
      45 | resource "aws_lambda_function" "hello_example" {
      46 |     filename = "code/hello_example.zip"
      47 |     description = "Example - terraform created lambda function"
      48 |     function_name = "hello_example"
      49 |     role = aws_iam_role.iam_lambda_role.arn
      50 |     handler = "lambda_function.lambda_handler"
      51 |
      52 |     source_code_hash = filebase64sha256("code/hello_example.zip")
      53 |     runtime = "python3.8"
      54 |
      55 |     environment {
      56 |         variables = {
      57 |             name = "Behzad"
      58 |         }
      59 |     }
      60 |     tags = var.tags
      61 | }
      62 |
      63 |
      64 | resource "aws_cloudwatch_event_rule" "cw_schedule_5m" {

  Impact:     WIthout full tracing enabled it is difficult to trace the flow of logs
  Resolution: Enable tracing

  More Info:
  - https://tfsec.dev/docs/aws/lambda/enable-tracing#aws/lambda
  - https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function#mode

  times
  ------------------------------------------
  disk i/o             13.1062ms
  parsing HCL          12.8µs
  evaluating values    3.7164ms
  running checks       7.541ms

  counts
  ------------------------------------------
  files loaded         2
  blocks               12
  modules              0

  results
  ------------------------------------------
  critical             0
  high                 0
  medium               0
  low                  1
  ignored              0

  1 potential problems detected.


```
