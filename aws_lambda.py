import json
import boto3

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

INSTANCE_ID = ['i-08c82fa04a688984e', 'i-03ed01cafa4e0f16b']
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:782818417694:EC2-Shutdown-Alert'

def lambda_handler(event, context):
    # message = {}
    for instance in INSTANCE_ID:
        #stop EC2
        ec2.stop_instances(InstanceIds=[instance])

        # Send SNS notification
        message= f"EC2 Instance{[INSTANCE_ID]} has been stopped successfully."

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="EC2 Shutdown Alert"
        )
    return {
        'statusCode': 200,
        'body': message
    }
