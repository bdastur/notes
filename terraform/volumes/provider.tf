provider "aws" {
    region = var.region
    shared_credentials_files = var.credentials_files
    profile = var.profile
}


terraform {
    backend "s3" {
        bucket = "tfstate-xxxxxxxx-bucket"
        key = "tfstates/testSetup/xxxxxx/testsetup.tfstate"
        region = "us-east-1"
        profile = "devOne" 
    }
}

