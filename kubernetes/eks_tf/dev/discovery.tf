/*
 * Get the Default VPC resource
 */
data "aws_vpc" "defaultVpc" {
  default = true
}

/*
 * Get the subnets in default vpc with
 * Tag "available": true
 * EKS is not supported in some AZ's hence the extra filter.
 */
data "aws_subnets" "subnets" { 
  filter {
    name = "vpc-id"
    values = [data.aws_vpc.defaultVpc.id]
  }
  filter {
    name = "tag:available"
    values = [true]
  }
}


