provider "aws" {
  region                  = var.region
  shared_credentials_files = var.credentials_files
  profile                 = var.profile
}

/** Backend **
terraform {
  backend "s3" {
    bucket = "<bucket name>"
    key    = "<path to tf state: eg: tfstates/sample/sample.tfstate>"
    kms_key_id = "<KMS KEY ARN>"
    region = "us-east-1"
    profile = "dev" 
  }
}
**/

