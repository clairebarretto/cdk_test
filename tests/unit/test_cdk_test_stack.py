import json
import pytest

from aws_cdk import core
from cdk_test.cdk_test_stack import CdkTestStack


def get_template():
    app = core.App()
    CdkTestStack(app, "cdk-test")
    return json.dumps(app.synth().get_stack("cdk-test").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
