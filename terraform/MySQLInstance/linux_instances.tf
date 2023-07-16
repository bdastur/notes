//Find the latest AL2 image.

data "aws_vpc" "defaultVpc" {
    default = true
}

data "aws_ami" "AL2Latest" {
    owners      = ["amazon"]
    most_recent = true
    filter {
        name = "name"
        values = ["al2023-ami-2023.0.20230503.0-kernel-6.1-x86_64"]
    }

    filter {
        name = "virtualization-type"
        values = ["hvm"]
    }
}


data "aws_ami" "MysqlLatest" {
    most_recent = true
    filter {
        name = "name"
        values = ["mysql-al2"]
    }

    filter {
        name = "virtualization-type"
        values = ["hvm"]
    }
}


data "cloudinit_config" "userData" {
    gzip          = true
    base64_encode = true

    # common user data.
    part {
        content_type = "text/x-shellscript"
        content = "${file("user_data/common.sh")}"
        filename = "/tmp/common.cfg"
    }
}

data "cloudinit_config" "bastionUserData" {
    gzip          = true
    base64_encode = true

    # common user data.
    part {
        content_type = "text/x-shellscript"
        content = "${file("user_data/bastion.sh")}"
        filename = "/tmp/bastion.cfg"
    }
}



resource "aws_instance" "testInstances" {
    count = var.linux_instances.count

    ami = data.aws_ami.AL2Latest.id
    key_name = var.linux_instances.keyName
    iam_instance_profile = aws_iam_instance_profile.LinuxInstanceProfile.name

    availability_zone = join("", [var.region, "a"])
    instance_type = var.linux_instances.instanceType
    vpc_security_group_ids = [aws_security_group.mysqlSG.id]
    root_block_device {
        delete_on_termination = true
        encrypted = true
        volume_type = var.rootVolume.type
        volume_size = var.rootVolume.size
        tags = {
            Name = "testInstRootVol-${count.index}"
        }
    }

    dynamic "ebs_block_device" {
        for_each = var.volumes

        content {
            delete_on_termination = true
            encrypted = true
            volume_type = ebs_block_device.value["type"]
            volume_size = ebs_block_device.value["size"]
            device_name = ebs_block_device.value["deviceName"]
            tags = {
                Name = "testInstVol-${count.index}"
            }
        }
    }

    tags = {
        Name = "TestInstance-${count.index}"
        Role = "TestInstance"
    }

    user_data = data.cloudinit_config.userData.rendered
}

resource "aws_instance" "bastionInstance" {
    ami      = data.aws_ami.AL2Latest.id
    key_name = var.linux_instances.keyName
    availability_zone = join("", [var.region, "a"])
    instance_type = "t3.micro"
    vpc_security_group_ids = [aws_security_group.bastionSG.id]

    tags = {
        Name = "Bastion-Instance"
        Role = "bastion"
    }

    user_data = data.cloudinit_config.bastionUserData.rendered
}


output "instance_ip_addr_0" {
    value = aws_instance.testInstances[*].public_ip
}

output "instance_dns" {
    value = aws_instance.testInstances[*].private_dns
}
