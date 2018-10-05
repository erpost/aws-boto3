import boto3
from pprint import pprint

client = boto3.client('s3')
pprint(client.exceptions.__dict__)

client = boto3.client('iam')
pprint(client.exceptions.__dict__)

client = boto3.client('sts')
pprint(client.exceptions.__dict__)
