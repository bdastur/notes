# EC2 Trust-relationship policy doc.
data "aws_iam_policy_document" "ec2AssumeRole" {
    statement {
        effect = "Allow"
        principals {
            type = "Service"
            identifiers = ["ec2.amazonaws.com"]
        }
        actions = ["sts:AssumeRole"]
    }
}


resource "aws_iam_role" "LinuxInstanceRole" {
    name = "TEST_LinuxInstanceRole"
    assume_role_policy = data.aws_iam_policy_document.ec2AssumeRole.json

    managed_policy_arns = [
        "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
    ]
}

resource "aws_iam_role" "WindowsInstanceRole" {
    name = "TEST_WindowsInstanceRole"
    assume_role_policy = data.aws_iam_policy_document.ec2AssumeRole.json

    managed_policy_arns = [
        "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
    ]
}

resource "aws_iam_role_policy" "VSSBackupPolicy" {
    name = "VSSBackupPolicy"
    role = aws_iam_role.WindowsInstanceRole.id

    # Policy definition.
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
          {
              Action = [
                  "ec2:DescribeInstances",
                  "ec2:CreateTags",
                  "ec2:CreateSnapshot"
              ]
              Effect = "Allow"
              Resource = "*"
          }
        ]
    })
}

resource "aws_iam_instance_profile" "LinuxInstanceProfile" {
    name = "TEST_LinuxInstanceProfile"
    role = aws_iam_role.LinuxInstanceRole.name
}


resource "aws_iam_instance_profile" "WindowsInstanceProfile" {
    name = "TEST_WindowsInstanceProfile"
    role = aws_iam_role.LinuxInstanceRole.name
}

