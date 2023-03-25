provider "aws" {
  region                  = var.region
  shared_credentials_files = var.credentials_files
  profile                 = var.profile
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

/*****************************************
 * Bucket definition.
 *****************************************/
resource "aws_s3_bucket" "testBucket" {
  bucket = "simple-bucket-1234-us-east-1"

 
  tags = {
    Name = "My Bucket"
    Environment = "Dev"
  }
}

/*****************************************
 * Bucket versioning configuration
 *****************************************/
resource "aws_s3_bucket_versioning" "versioningOn" {
  bucket = aws_s3_bucket.testBucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

/*****************************************
 * Bucket lifecyle configuration.
 *****************************************/
resource "aws_s3_bucket_lifecycle_configuration" "example" {
  bucket = aws_s3_bucket.testBucket.id

  rule {
    id = "rule-on-prefix-logs"
    status = "Enabled"
    filter {
      prefix = "logs/"
    }
    transition {
      days = 30
      storage_class = "STANDARD_IA"
    }
    transition {
      days = 60
      storage_class = "GLACIER"
    }
    expiration {
      days = 90
    }
  }
}
