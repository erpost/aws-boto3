import boto3

profile = 'jau-sec-admin'
region = 'us-east-1'

boto3.setup_default_session(profile_name=profile)
ec2 = boto3.resource('ec2', region_name=region)

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)


# Stop all running Instances
#ec2.instances.filter(InstanceIds=ids).stop()

# Terminate all running instances
#ec2.instances.filter(InstanceIds=ids).terminate()
