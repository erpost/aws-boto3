import boto3
from pprint import pprint


# get profiles of all Security Hub Accounts
master_profile = input('Provide the master account profile\n'
                       'Default is "audit": ')
if len(master_profile) < 1:
    master_profile = 'audit'

log_profile = input('Provide the logging account profile\n'
                    'Default is "log": ')
if len(log_profile) < 1:
    log_profile = 'log'

member_profiles = input('Provide a comma-separated list of member account profiles\n'
                        'Default is "sub1, root": ')
if len(member_profiles) < 1:
    member_profiles = 'sub1, root'
member_profiles_list = [member_profile.strip() for member_profile in member_profiles.split(",")]

# get all regions where Security Hub is enabled
primary_region = input('Provide the Security Hub Primary Region.\n'
                       'Default is "us-east-1": ')
if len(primary_region) < 1:
    primary_region = 'us-east-1'

secondary_regions = input('Provide a comma-separated list of AWS regions where Security Hub is enabled.\n'
                          'Default is "us-east-2, us-west-1, us-west-2": ')
if len(secondary_regions) < 1:
    secondary_regions = 'us-east-2,us-west-1,us-west-2'
secondary_regions_list = [region.strip() for region in secondary_regions.split(",")]


# controls to be disabled in all
disable_control_ids = ['CIS.1.1', 'CIS.1.2', 'CIS.1.3', 'CIS.1.4', 'CIS.1.5', 'CIS.1.6', 'CIS.1.7', 'CIS.1.8',
                       'CIS.1.9', 'CIS.1.10', 'CIS.1.11', 'CIS.1.12', 'CIS.1.13', 'CIS.1.14', 'CIS.1.16', 'CIS.1.20',
                       'CIS.1.22', 'CIS.2.4', 'CIS.2.5', 'CIS.3.1', 'CIS.3.2', 'CIS.3.3', 'CIS.3.4', 'CIS.3.5',
                       'CIS.3.6', 'CIS.3.7', 'CIS.3.8', 'CIS.3.9', 'CIS.3.10', 'CIS.3.11', 'CIS.3.12', 'CIS.3.13',
                       'CIS.3.14']

print('Master Profile:', master_profile)
print('Logging Profile:', log_profile)
print('Member Profiles:', member_profiles_list)
print('\nPrimary Region:', primary_region)
print('Secondary Region:', secondary_regions_list)
print('Disabled Controls:', disable_control_ids)
