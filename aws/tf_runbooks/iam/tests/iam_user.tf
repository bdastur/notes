resource "aws_iam_user" "testuser_1" {
    name = "testuser_1"
    path = "/operations/"
    
    tags = {
        Project = "Rampup"
        Team    = "Kafka"
    }
}

resource "aws_iam_access_key" "key" {
    user = aws_iam_user.testuser_1.name
}

