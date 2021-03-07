# Terraform


## Links
* [Variables](https://www.terraform.io/docs/configuration/variables.html)
* [Infra cost - Get cost estimates for terraform projects](https://github.com/infracost/infracost)


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



