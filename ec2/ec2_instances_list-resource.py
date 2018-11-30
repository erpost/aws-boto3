import boto3


def get_regions():
    client = boto3.client('ec2')
    regions = []
    response = client.describe_regions()
    for region in response['Regions']:
        regions.append(region['RegionName'])
    return regions


for aws_region in get_regions():
    ec2 = boto3.resource('ec2', region_name=aws_region)
    print('#' * 10, aws_region, '#' * 10)
    for instance in ec2.instances.all():
        print(instance.id, ':', instance.state['Name'])
        if instance.tags is None:
            print('No Tags')
        else:
            tag_dict = {}
            for tags in instance.tags:
                tag_dict[tags['Key']] = tags['Value']
            print(tag_dict)
