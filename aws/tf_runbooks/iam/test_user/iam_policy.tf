resource "aws_iam_policy" "allow_policy" {
    name = "mp_allow_operations"
    path = "/"
    description = "Allow operations team access"

    policy = file("allow_operations_selfservice.json")
}

resource "aws_iam_policy_attachment" "policy_attach" {
  name       = "policy-attachment"
  users      = [aws_iam_user.cloudops.name]
  policy_arn = aws_iam_policy.allow_policy.arn
}
