import boto3

profile = ''
region = ''

boto3.setup_default_session(profile_name=profile)
ec2 = boto3.resource('ec2', region_name=region)

for instance in ec2.instances.all():
    print(instance.id, instance.state)
