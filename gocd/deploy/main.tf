provider "aws" {
  region                  = var.region
  shared_credentials_file = var.credentials_file
  profile                 = var.profile
}


terraform {
  required_version = ">= v0.11.7"
    backend "s3" {
      region     = "us-west-2"
      profile    = "dev1"
      bucket     = "dev1-temp"
      key        = "tfstates/gocd-env/sandbox.tfstate"
      encrypt    = "false"
      acl        = "bucket-owner-full-control"
    }
}

