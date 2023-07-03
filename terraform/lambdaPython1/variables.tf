###########################################################
# Common Variables
###########################################################
variable "credentials_files" {
  type    = list 
  default = ["$HOME/.aws/credentials"]
}

variable "profile" {
  type    = string
}

variable "region" {
  type    = string
}

