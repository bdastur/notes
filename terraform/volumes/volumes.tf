resource "aws_ebs_volume" "testVolumeBatch" {
  count = var.volumeSpec.count 
  availability_zone = var.volumeSpec.az 
  size              = var.volumeSpec.size 
  encrypted = true
  type = var.volumeSpec.type 

  tags = {
    Name = "TestVolume-${count.index}"
    TerraformManaged = true
  }
}


resource "aws_ebs_snapshot" "testSnapshotBatchOne" {
  for_each = toset(aws_ebs_volume.testVolumeBatch[*].id)
  volume_id = each.key 

  tags = {
    Name = "TestSnapshot-${each.key}"
  }
}

resource "aws_ebs_snapshot" "testSnapshotBatchTwo" {
  for_each = toset(aws_ebs_volume.testVolumeBatch[*].id)
  volume_id = each.key

  tags = {
    Name = "TestSnapshot-${each.key}"
  }
}

resource "aws_ebs_snapshot" "testSnapshotBatchThree" {
  for_each = toset(aws_ebs_volume.testVolumeBatch[*].id)
  volume_id = each.key

  tags = {
    Name = "TestSnapshot-${each.key}"
  }
}

resource "aws_ebs_snapshot" "testSnapshotForAmi" {
  volume_id = aws_ebs_volume.testVolumeBatch[0].id 

  tags = {
    Name = "TestSnapshotForAmi"
  }

}


resource "aws_ami" "testAmiBatch" {
  count = var.amiSpec.count

  name = "TestAmiDLM-${count.index}"
  virtualization_type = "hvm"
  root_device_name = "/dev/xvda"
  ebs_block_device {
    device_name = var.amiSpec.deviceName
    snapshot_id = aws_ebs_snapshot.testSnapshotForAmi.id
  }
}

