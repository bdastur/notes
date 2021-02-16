#########################################################                       
# SSH Access
#########################################################                       
resource "aws_security_group" "sandbox_sgrule_ssh_access" {
  name        = "${var.sandbox_name}-ssh-access-secgroup"
  description = "Sandbox Ingress ssh security group"
  vpc_id      = aws_vpc.sandbox_vpc.id

  tags = {
    Name     = join("_", [var.tags["sandbox_name"], "sshaccess"])
    stack    = var.tags["Stack"]
  }
}


#########################################################
# GoCD Access
#########################################################
resource "aws_security_group" "sandbox_sgrule_gocd_http_access" {
  name        = "${var.sandbox_name}-gocd-access-secgroup"
  description = "Sandbox Ingress GoCD security group"
  vpc_id      = aws_vpc.sandbox_vpc.id

  tags = {
    Name     = join("_", [var.tags["sandbox_name"], "promaccess"])
    stack    = var.tags["Stack"]
  }
}


#########################################################
# INGRESS Security group rules (ssh access)
#########################################################
resource "aws_security_group_rule" "secgroup_ssh_access" {
  description = "Allow SSH ingress from allowed subnets"
  type        = "ingress"
  from_port   = 22
  to_port     = 22
  protocol    = "tcp"

  security_group_id = aws_security_group.sandbox_sgrule_ssh_access.id
  cidr_blocks       = var.ssh_cidrs
}

#########################################################
# INGRESS Security group rules (TCP 9090 access)
#########################################################
resource "aws_security_group_rule" "secgroup_gocd_access" {
  description = "Allow Prometheus ingress from allowed subnets"
  type        = "ingress"
  from_port   = 80
  to_port     = 9190 
  protocol    = "tcp"

  security_group_id = aws_security_group.sandbox_sgrule_gocd_http_access.id
  cidr_blocks       = var.access_cidrs
}


#########################################################
# EGRESS Security group rules
#########################################################
resource "aws_security_group_rule" "secgroup_egress_allow_all" {
  description = "Allow egress "
  type        = "egress"
  from_port   = -1
  to_port     = -1
  protocol    = "all"

  security_group_id = aws_security_group.sandbox_sgrule_ssh_access.id
  cidr_blocks       = ["${var.cidr_block}"]
}

resource "aws_security_group_rule" "secgroup_egress_external" {
  description = "Allow TCP egress"
  type        = "egress"
  from_port   = 0
  to_port     = 65535
  protocol    = "tcp"

  security_group_id = aws_security_group.sandbox_sgrule_ssh_access.id
  cidr_blocks       = ["0.0.0.0/0"]
}

