import boto3

profile = 'sub1'
region = 'us-east-1'
running_ids = []

boto3.setup_default_session(profile_name=profile)
ec2 = boto3.resource('ec2', region_name=region)

running_instances = ec2.instances.filter(
                    Filters=[{'Name': 'instance-state-name', 'Values': ['running']},
                             {'Name': 'tag:sandman', 'Values': ['true']}
                             ])

for running_instance in running_instances:
    running_ids.append(running_instance.id)

print(running_ids)

ec2.instances.filter(InstanceIds=running_ids).stop()

# Can also set filtering for opposite (only shutdown instances without the Sandman Tag)
#
# all_running_instances = ec2.instances.filter(
#     Filters=[
#         {'Name': 'instance-state-name', 'Values': ['running']}
#     ]
# )
#
# sandman_instances = ec2.instances.filter(
#     Filters=[
#         {'Name': 'instance-state-name', 'Values': ['running']},
#         {'Name': 'tag:sandman', 'Values': ['true']}
#     ]
# )
#
# non_sandman_instances = set(all_running_instances).difference(set(snadman_instances))