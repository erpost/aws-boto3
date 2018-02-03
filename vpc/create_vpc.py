import boto3

profile = input('AWS Profile [default]: ')
if len(profile) < 1:
    profile = 'default'

region = input('VPC Region [us-east-1]: ')
if len(region) < 1:
    region = 'us-east-1'

vpccidr = input('VPC CIDR [10.0.0.0/16]: ')
if len(vpccidr) < 1:
    vpccidr = '10.0.0.0/16'

subcidr = input('Subnet CIDR [10.0.0.0/24]: ')
if len(subcidr) < 1:
    subcidr = '10.0.0.0/24'

inboundips = input('Inbound IPs Allowed [0.0.0.0/0]: ')
if len(inboundips) < 1:
    inboundips = ''

boto3.setup_default_session(profile_name=profile)
ec2 = boto3.resource('ec2', region_name=region)

# Create VPC and Subnet"
vpc = ec2.create_vpc(CidrBlock=vpccidr)
ec2.create_tags(Resources=[vpc.vpc_id], Tags=[{'Key': 'Name', 'Value': 'VPC-Test'}])
print('VPC "{}" has been created'.format(vpc.vpc_id))

subnet = vpc.create_subnet(CidrBlock=subcidr)
ec2.create_tags(Resources=[subnet.id], Tags=[{'Key': 'Name', 'Value': 'Subnet-Test'}])
print('Subnet "{}" has been created'.format(subnet.id))

# Create Gateway
internet_gateway = ec2.create_internet_gateway()
internet_gateway.attach_to_vpc(VpcId=vpc.vpc_id)
ec2.create_tags(Resources=[internet_gateway.internet_gateway_id], Tags=[{'Key': 'Name', 'Value': 'GW-Test'}])
print('Internet Gateway "{}" has been created'.format(internet_gateway.internet_gateway_id))

# Create Route Table, Route and associate with VPC
route_table = vpc.create_route_table()
route_ig_ipv4 = route_table.create_route(DestinationCidrBlock='0.0.0.0/0',
                                         GatewayId=internet_gateway.internet_gateway_id)
route_table.associate_with_subnet(SubnetId=subnet.id)
ec2.create_tags(Resources=[route_table.id], Tags=[{'Key': 'Name', 'Value': 'RouteTable-Test'}])
print('Route Table "{}" has been created'.format(route_table.id))

# Create Security Group
sg = ec2.create_security_group(GroupName='Security-Group-Test', Description="Open Security Group 3389 & 22", VpcId=vpc.vpc_id)

ip_ranges = [{
    'CidrIp': inboundips
}]

perms = [{
    'IpProtocol': 'TCP',
    'FromPort': 3389,
    'ToPort': 3389,
    'IpRanges': ip_ranges
}, {
    'IpProtocol': 'TCP',
    'FromPort': 22,
    'ToPort': 22,
    'IpRanges': ip_ranges
}]

# ec2.create_tags(Resources=[security_group_id], Tags=[{'Key': 'Name', 'Value': 'SecurityGroup-Test'}])
# print('Security Group "{}" has been created'.format(security_group_id))
sg.authorize_ingress(IpPermissions=perms)

