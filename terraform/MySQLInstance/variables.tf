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

###########################################################
# Instance specific variables.
###########################################################

variable "linux_instances" {
    type = map
}

variable "rootVolume" {
    type = map
}

variable "volumes" {
    type = list
}

