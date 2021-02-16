/*data "template_file" "cloudinit" {
    template="file("./scripts/cloud_config.yaml")

}
*/


###########################################################
# Sandbox Launch template
###########################################################
resource "aws_launch_template" "sandbox_lt" {
  name_prefix   = "sandbox_lt"
  instance_type = var.asg_1["instance_type"]
  image_id      = var.asg_1["ami_id"]

  block_device_mappings {
    device_name = "/dev/sda1"
    ebs {
      volume_size = var.asg_1["volume_size"] 
      volume_type = var.asg_1["volume_type"] 
    }
  }

  ebs_optimized          = true
  key_name               = var.asg_1["key_name"] 
  vpc_security_group_ids = [aws_security_group.sandbox_sgrule_ssh_access.id,
                            aws_security_group.sandbox_sgrule_gocd_http_access.id]
  user_data = filebase64("./scripts/cloud_config.yaml")

  lifecycle {
    create_before_destroy = true
  }
}

###########################################################
# Autoscaling group
###########################################################
resource "aws_autoscaling_group" "sandbox_asg" {
  depends_on = [
    aws_launch_template.sandbox_lt
  ]
  name_prefix = "sandbox-asg"

  vpc_zone_identifier       = [aws_subnet.az1.id, aws_subnet.az2.id]
  min_size                  = var.asg_1["min_size"]
  max_size                  = var.asg_1["max_size"]
  desired_capacity          = var.asg_1["desired_capacity"]
  health_check_grace_period = var.asg_1_health_check["grace_period"]
  health_check_type         = "EC2"
  termination_policies      = ["OldestInstance", "OldestLaunchConfiguration"]
  target_group_arns         = [""]
  load_balancers            = [""]

  launch_template {
    id      = aws_launch_template.sandbox_lt.id
    version = "$Latest"
  }

  lifecycle {
    create_before_destroy = true
  }

  tags = var.asg_1_tags

}

