
/*
 * IAM Lambda Role
 */
resource "aws_iam_role" "lambdaOneRole" {
    name = "lambdaOneRole"
    
    assume_role_policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Action = "sts:AssumeRole"
          Effect = "Allow"
          Sid = "lambdaoneRoleStmt1"
          Principal = {
            Service = "lambda.amazonaws.com"
          }
        }
      ]
    })

    tags = {
        Name = "lambdaOneRole"
        Environment = "Dev"
    }
}

/*
 * Local file 
 */
data "archive_file" "lambdaOneCode" {
  type = "zip"
  source_file = "source/main.py"
  output_path = "bin/lambda_payload.zip"
}

resource "aws_lambda_function" "lambdaOne" {
  function_name = "testLambdaOne"
  description = "This is a test function for TF test"
  role = aws_iam_role.lambdaOneRole.arn 

  #Specifying code.
  filename = data.archive_file.lambdaOneCode.output_path
  handler = "main.handler"

  runtime = "python3.9"
  architectures = ["x86_64"]
  
  
}



