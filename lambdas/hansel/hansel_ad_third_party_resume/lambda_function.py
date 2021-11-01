import boto3
import json
import os

sns = boto3.resource('sns', region_name=os.getenv('AWS_REGION'))

def lambda_handler(event, context):

    # Testing permissions - SNS Publish to Hansel-Error
    topic = sns.Topic('arn:aws:sns:us-west-2:706698525731:hansel-stack-HanselErrorEE623DBD-JLTLS3YCZ6FS')
    topic.publish(
        Message=json.dumps(event, indent=4),
        Subject='A test message from Hansel-Error...')

    # Testing permissions - SNS Publish to Gasfight-API-Queue
    topic = sns.Topic('arn:aws:sns:us-west-2:706698525731:gasfight-stack-GasFightQueueAPIRequestAB141C88-1P2BYWCLFSQDK')
    topic.publish(
        Message=json.dumps(event, indent=4),
        Subject='A test message from GasFight-API...')

    return {
        'statusCode': 200,
        'body': 'Test function'
    }