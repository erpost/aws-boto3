import boto3

profile = ''
aws_region = ''

boto3.setup_default_session(profile_name=profile)


def get_regions():
    client = boto3.client('ec2', region_name=aws_region)
    regions = []
    response = client.describe_regions()
    for region in response['Regions']:
        regions.append(region['RegionName'])
    return regions


def get_volumes():
    for region in get_regions():
        ec2 = boto3.resource('ec2', region_name=region)
        volumes = ec2.volumes.all()
        print(region)
        for volume in volumes:
            print(volume.id)


if __name__ == '__main__':
    # print(get_regions())
    print(get_volumes())
