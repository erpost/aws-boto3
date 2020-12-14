from pprint import pprint
import boto3

profiles = boto3.session.Session().available_profiles
boto3.setup_default_session(profile_name=profiles[0], region_name='us-east-1')
sts_client = boto3.client('sts')

pprint(sts_client.get_caller_identity())
account_id = sts_client.get_caller_identity()["Account"]
pprint(account_id)
