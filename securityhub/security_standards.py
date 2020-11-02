from pprint import pprint
import boto3


profile = 'sub1'
region = 'us-east-1'


def describe_standards():
    boto3.setup_default_session(profile_name=profile)
    sh_client = boto3.client('securityhub', region_name=region)
    standards = sh_client.describe_standards()['Standards']

    return standards



if __name__ == '__main__':
    pprint(describe_standards())
