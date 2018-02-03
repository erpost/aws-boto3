import boto3

profile = ''
region = ''

boto3.setup_default_session(profile_name=profile)
ec2 = boto3.resource('ec2', region_name=region)

instance = ec2.create_instances(
    ImageId='ami-a7aa15c3',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')
print(instance[0].id)
