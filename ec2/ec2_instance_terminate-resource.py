# call script from cli: python3 terminate_instance.py <Instance ID>

import sys
import boto3

profile = ''
region = ''

boto3.setup_default_session(profile_name=profile)
ec2 = boto3.resource('ec2', region_name=region)

for instance_id in sys.argv[1:]:
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    print(response)
