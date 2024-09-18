import aws_cdk as core
import aws_cdk.assertions as assertions

from installer_spam_score.installer_spam_score_stack import InstallerSpamScoreStack

# example tests. To run these tests, uncomment this file along with the example
# resource in installer_spam_score/installer_spam_score_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = InstallerSpamScoreStack(app, "installer-spam-score")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
