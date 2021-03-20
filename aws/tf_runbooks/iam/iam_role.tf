data "aws_iam_policy_document" "ec2_assume_role" {
    statement {
        sid    = ""
        effect  = "Allow"
        actions = ["sts:AssumeRole"]
        principals {
            type        = "Service"
            identifiers = ["ec2.amazonaws.com"]
        }
    }
}


resource "aws_iam_role" "test_ec2_role" {
    name = "testrole_brd"
    description = "This is a test role"
    assume_role_policy = data.aws_iam_policy_document.ec2_assume_role.json

}

