import boto3
import csv


outfile = 'prod-instances.csv'

with open(outfile, 'w', newline='') as outfile:
    out_file = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    out_file.writerow(['Instance Name'] + ['Instance ID'] + ['Region'] + ['Instance State'] +
                      ['Private DNS'] + ['Public DNS'] + ['Environment'] + ['Tags'])


    def get_regions():
        client = boto3.client('ec2')
        regions = []
        response = client.describe_regions()
        for region in response['Regions']:
            regions.append(region['RegionName'])
        return regions


    for aws_region in get_regions():
        ec2 = boto3.resource('ec2', region_name=aws_region)
        for instance in ec2.instances.all():
            tag_dict = {}
            name_tag = ''
            env_tag = ''
            print('Instance ID: ', instance.id)
            print('Region: ', aws_region)
            print('Instance State: ', instance.state['Name'])
            try:
                print('Private DNS: ', instance.private_dns_name)
                priv_dns = instance.private_dns_name
            except AttributeError:
                print('Private DNS: None')
                priv_dns = 'None'
            try:
                print('Public DNS: ', instance.public_dns)
                pub_dns = instance.public_dns
            except AttributeError:
                print('Public DNS: None')
                pub_dns = 'None'
            if instance.tags is None:
                print('No Tags')
            else:
                for tags in instance.tags:
                    if tags['Key'] == 'Name':
                        name_tag = tags['Value']
                    if tags['Key'] == 'Environment':
                        env_tag = tags['Value']
                    tag_dict[tags['Key']] = tags['Value']
                print(tag_dict)
            out_file.writerow([name_tag] + [instance.id] + [aws_region] +
                              [instance.state['Name']] +[priv_dns] + [pub_dns] + [env_tag] + [tag_dict])
