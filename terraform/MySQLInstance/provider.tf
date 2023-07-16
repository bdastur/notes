provider "aws" {
    region = var.region
    shared_credentials_files = var.credentials_files
    profile = var.profile
}


terraform {
    backend "s3" {
        bucket = "BUCKET_NAME_REPLACE"
        key = "tfstates/testSetup/mysqlinstance/testsetup.tfstate"
        region = "us-east-1"
        profile = "PROFILE_REPLACE" 
    }
}

