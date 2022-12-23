import aws_cdk as core
import aws_cdk.assertions as assertions

from simple_app.simple_app_stack import SimpleAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in simple_app/simple_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SimpleAppStack(app, "simple-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
