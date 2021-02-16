###########################################################
# Common Variables
###########################################################
variable "sandbox_name" {
    description = "Identifier for the sandbox. Adds tag Sandbox with this value"
    type = string
}

variable "credentials_file" {
  type    = string
  default = "$HOME/.aws/credentials"
}

variable "profile" {
  type    = string
}

variable "region" {
  type    = string
}

###########################################################
# VPC Variables.
###########################################################
variable "cidr_block" {
    type = string
}

variable "instance_tenancy" {
    type = string
}

variable "enable_dns_support" {
    type = bool
}

variable "enable_dns_hostnames" {
    type = bool
}

variable "tags" {
    type = map
}

###########################################################
# Subnet Variables.
###########################################################
variable "subnet_cidr_blocks" {
    type = list
}

variable "subnet_azs" {
    type = list
}

variable "map_public_ip_on_launch" {
    type = bool
}


###########################################################
# Security group Variables.
###########################################################
variable "ssh_port_open" {
    type = bool
}

variable "ssh_cidrs" {
    type = list
}

variable "https_port_open" {
    type = bool
    default = false
}

variable "https_cidrs" {
    type = list
    default = []
}

variable "access_cidrs" {
    type = list
    default = []
}

###########################################################
# ASG.
###########################################################
variable "asg_1" {
    type = map
}

variable "asg_1_tags" {
 type = list(any)
}

variable "asg_1_health_check" {
    type = map
}

