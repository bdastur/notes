data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["eks.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "eksRole" {
  name               = "eksClusterAssumeRole"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_iam_role_policy_attachment" "eksRole-AmazonEKSClusterPolicy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.eksRole.name
}




resource "aws_eks_cluster" "testCluster" {
  name = "testcluster"
  role_arn = aws_iam_role.eksRole.arn  

  vpc_config {
    subnet_ids = data.aws_subnets.subnets.ids
  }

  tags = {
    application = "Test"
  }
}

output "endpoint" {
  value = aws_eks_cluster.testCluster.endpoint
}

output "oidcIssuer" {
  value = aws_eks_cluster.testCluster.identity[*]
}
