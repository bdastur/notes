resource "aws_cloudwatch_log_group" "simpleApiLogGroup" {
  name_prefix = "simpleApi_LogGroup"
  retention_in_days = 3

  tags = {
    Environment = "dev"
    Application = "TestApp"
  }
}
