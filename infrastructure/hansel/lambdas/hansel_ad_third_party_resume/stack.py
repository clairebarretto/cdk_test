import os
from aws_cdk import (
    core,
    aws_events as _events,
    aws_events_targets as _targets,
    aws_lambda as _lambda,
    aws_sns as _sns
)
from dotenv import load_dotenv

load_dotenv()

class HanselAdThirdPartyResumeStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn_name = 'hansel_ad_third_party_resume'

        # ------------------------------------
        # Lambda
        # ------------------------------------

        # Create new lambda function
        lambda_fn = _lambda.Function(self, 'lambda',
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler='lambda_function.lambda_handler',
            code=_lambda.Code.from_asset(f'lambdas/hansel/{fn_name}'))

        # ------------------------------------
        # Triggers
        # ------------------------------------

        # CloudWatch event that will trigger the lambda function every 15 mins
        rule = _events.Rule(self, f'rule-{fn_name}',
            schedule=_events.Schedule.rate(core.Duration.minutes(15)))
        rule.add_target(_targets.LambdaFunction(lambda_fn))

        # ------------------------------------
        # Permissions
        # ------------------------------------

        # Publish to Hansel error topic
        topic = _sns.Topic.from_topic_arn(self, 'HanselError',
            topic_arn=os.getenv('HANSEL_SNS_TOPIC_ERROR'))
        topic.grant_publish(lambda_fn)

        # Publish to GasFight API queue topic
        topic = _sns.Topic.from_topic_arn(self, 'GasFightAPI',
            topic_arn=os.getenv('GASFIGHT_SNS_QUEUE_API_REQUEST'))
        topic.grant_publish(lambda_fn)
