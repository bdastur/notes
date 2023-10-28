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

variable "volumeSpec" {
    type = map 
}

variable "snapshotSpec" {
    type = map
}

variable "amiSpec" {
    type = map
}

