resource "aws_sns_topic" "billing_alert_topic" {
  name = "sns-billing-topic"
  display_name = "BillingTopic"
  
}

resource "aws_cloudwatch_metric_alarm" "billing_alarm" {
  alarm_name                = "cloudwatch-billing-alarm-10usd"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = "EstimatedCharges"
  namespace                 = "AWS/Billing"
  period                    = "21600"
  statistic                 = "Maximum"
  threshold                 = "10"
  alarm_description         = "Alert when EstimatedCharges exceeds 10USD"
  alarm_actions             = ["${aws_sns_topic.billing_alert_topic.arn}"]
  insufficient_data_actions = []
}
