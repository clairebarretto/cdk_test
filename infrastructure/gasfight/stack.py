from aws_cdk import (
    core,
    aws_sns as _sns,
)

class GasFightStack(core.Stack):

    def __init__(self, scope: core.Stack, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        ##################################
        # SNS
        ##################################

        _sns.Topic(self, 'GasFight-Queue-API-Request')
        _sns.Topic(self, 'GasFight-Error')
