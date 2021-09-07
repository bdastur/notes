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

variable "tags" {
    type = map
}
