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

data "aws_iam_policy_document" "ec2_service_assume_role" {
  statement {
    effect = "Allow"
    principals {
      type = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

/*
 * IAM Role for EKS Cluster.
 */
resource "aws_iam_role" "eksRole" {
  name               = "eksClusterAssumeRole"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_iam_role_policy_attachment" "eksRole-AmazonEKSClusterPolicy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.eksRole.name
}

/*
 * IAM Role for EKS Node groups
 */
resource "aws_iam_role" "eksNodeRole" {
  name = "eksNodeGroupAssumeRole"
  assume_role_policy = data.aws_iam_policy_document.ec2_service_assume_role.json
}

resource "aws_iam_role_policy_attachment" "eksNodeRole_ECR_PolicyAttachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  role = aws_iam_role.eksNodeRole.name
}

resource "aws_iam_role_policy_attachment" "eksNodeRole_CNI_PolicyAttachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
  role = aws_iam_role.eksNodeRole.name
}

resource "aws_iam_role_policy_attachment" "eksNodeRole_EKSCluster_PolicyAttachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role = aws_iam_role.eksNodeRole.name
}

resource "aws_iam_role_policy_attachment" "eksNodeRole_EKSWorkerNode_PolicyAttachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
  role = aws_iam_role.eksNodeRole.name
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
output "clusterName" {
  value = aws_eks_cluster.testCluster.name
}

output "endpoint" {
  value = aws_eks_cluster.testCluster.endpoint
}

output "oidcIssuer" {
  value = aws_eks_cluster.testCluster.identity[0]
}

output "connectCommand" {
  value = "aws eks update-kubeconfig --region us-east-1 --name ${aws_eks_cluster.testCluster.name} --profile ${var.profile}"
}


resource "aws_eks_node_group" "smallNodes" {
  cluster_name = aws_eks_cluster.testCluster.name
  node_group_name = "smallNodes"
  subnet_ids = data.aws_subnets.subnets.ids
  node_role_arn   = aws_iam_role.eksNodeRole.arn

  scaling_config {
    desired_size = 2
    max_size = 2
    min_size = 1
  }
}
