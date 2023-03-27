provider "aws" {
  region                  = var.region
  shared_credentials_files = var.credentials_files
  profile                 = var.profile
}

terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
    }
  }
}

terraform {
  backend "s3" {
    bucket = "cwbench-terraform-state-us-east-1"
    key    = "tfstates/sample/sample.tfstate"
    kms_key_id = "arn:aws:kms:us-east-1:462972568455:alias/tfkey"
    region = "us-east-1"
    profile = "dev" 
  }
}

