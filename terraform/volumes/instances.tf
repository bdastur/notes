# ------------------------ Instances ------------------------
resource "aws_instance" "TestInstanceBatchOne" {
    count = var.instanceSpecA.count 

    ami = var.instanceSpecA.ami
    availability_zone = var.instanceSpecA.az 
    instance_type = var.instanceSpecA.type 
    root_block_device {
        delete_on_termination = true
        encrypted = true
        volume_type = "gp3" 
        volume_size = var.instanceSpecA.size 
        tags = {
            Name = "TestInstanceBatchOne-${count.index}"
        }
    }
        tags = {
        Name = "TestInstance-${count.index}"
        Role = "TestInstance"
    }
}

resource "aws_instance" "TestInstanceBatchTwo" {
    count = var.instanceSpecB.count 

    ami = var.instanceSpecA.ami 
    availability_zone = var.instanceSpecB.az 
    instance_type = var.instanceSpecB.type 
    root_block_device {
        delete_on_termination = true
        encrypted = true
        volume_type = "gp3" 
        volume_size = var.instanceSpecB.size 
        tags = {
            Name = "TestInstanceBatchTwo-${count.index}"
        }
    }
        tags = {
        Name = "TestInstance-${count.index}"
        Role = "TestInstance"
    }
}

# ------------------- AMIs ------------------------------------
# Create AMIs from instances.

resource "aws_ami_from_instance" "TestAMIFromInstanceBatchOneA" {
    for_each = toset(aws_instance.TestInstanceBatchOne[*].id)

    name = "TestAMIInstanceOneA"
    source_instance_id = each.key
}

resource "aws_ami_from_instance" "TestAMIFromInstanceBatchOneB" {
    for_each = toset(aws_instance.TestInstanceBatchOne[*].id)

    name = "TestAMIInstanceOneB"
    source_instance_id = each.key
}

