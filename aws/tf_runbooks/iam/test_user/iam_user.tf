resource "aws_iam_user" "cloudops" {
    name = "cloudops"
    path = "/operations/"
    
    tags = {
        Project = "Rampup"
        Team    = "Kafka"
    }
}

resource "aws_iam_access_key" "key" {
    user = aws_iam_user.cloudops.name
}

