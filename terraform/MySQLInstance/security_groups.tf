resource "aws_security_group" "mysqlSG" {
    name        = "mysql_security_group"
    description = "Allow SSH, Mysql traffic"
    vpc_id      = data.aws_vpc.defaultVpc.id
}

resource "aws_security_group" "bastionSG" {
    name        = "bastion_security_group"
    description = "Allow SSH"
    vpc_id      = data.aws_vpc.defaultVpc.id
}

resource "aws_security_group_rule" "BastionAllowSSH" {
    type              = "ingress"
    from_port         = 22
    to_port           = 22
    protocol          = "tcp"
    cidr_blocks       = ["0.0.0.0/0"]
    security_group_id = aws_security_group.bastionSG.id
}


resource "aws_security_group_rule" "MysqlAallowSSH" {
    type              = "ingress"
    from_port         = 22 
    to_port           = 22 
    protocol          = "tcp"
    cidr_blocks       = ["0.0.0.0/0"]
    security_group_id = aws_security_group.mysqlSG.id
}

resource "aws_security_group_rule" "IngressallowMySQL" {
    type              = "ingress"
    from_port         = 3306 
    to_port           = 3306 
    protocol          = "tcp"

    source_security_group_id = aws_security_group.bastionSG.id
    security_group_id        = aws_security_group.mysqlSG.id

}

resource "aws_security_group_rule" "BastionEgressAllowAll" {
    type            = "egress"
    from_port       = -1
    to_port         = -1
    protocol        = "all"
    cidr_blocks     = ["0.0.0.0/0"]
    security_group_id = aws_security_group.bastionSG.id
}

resource "aws_security_group_rule" "MysqlEgressAllowAll" {
    type            = "egress"
    from_port       = -1
    to_port         = -1
    protocol        = "all"
    cidr_blocks     = ["0.0.0.0/0"]
    security_group_id = aws_security_group.mysqlSG.id
}

