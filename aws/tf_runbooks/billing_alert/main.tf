provider "aws" {
  region                  = var.region
  shared_credentials_file = var.credentials_file
  profile                 = var.profile
}


