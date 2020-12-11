import boto3
from pprint import pprint


# get profiles of all Security Hub Member Accounts
def get_member_profiles():
    member_profiles = input('Provide a comma-separated list of member account profiles\n'
                            'Default is "sub1, root": ')
    if len(member_profiles) < 1:
        member_profiles = 'sub1, root'
    member_profiles_list = [member_profile.strip() for member_profile in member_profiles.split(",")]

    return member_profiles_list


# get all regions where Security Hub is enabled
def get_regions():
    regions = input('Provide a comma-separated list of AWS regions where Security Hub is enabled.\n'
                    'DO NOT Include the Security Hub Primary Region\n'
                    'Default is "us-east-2, us-west-1, us-west-2": ')
    if len(regions) < 1:
        regions = 'us-east-2,us-west-1,us-west-2'
    regions_list = [region.strip() for region in regions.split(",")]

    return regions_list


# get list of controls to disable
def get_controls_to_disable():
    disabled = input('Provide a comma-separated list of CIS control IDs to disable. Default is:\n'
                     'CIS.1.1, CIS.1.2, CIS.1.3, CIS.1.4, CIS.1.5, CIS.1.6, CIS.1.7, CIS.1.8,\n'
                     'CIS.1.9, CIS.1.10, CIS.1.11, CIS.1.12, CIS.1.13, CIS.1.14, CIS.1.16, CIS.1.20, CIS.1.22,\n'
                     'CIS.2.4, CIS.2.5, CIS.2.7, CIS.3.1, CIS.3.2, CIS.3.3, CIS.3.4, CIS.3.5, CIS.3.6, CIS.3.7,\n'
                     'CIS.3.8, CIS.3.9, CIS.3.10, CIS.3.11, CIS.3.12, CIS.3.13, CIS.3.14\n\nPlease input list: ')
    if len(disabled) < 1:
        disabled = 'CIS.1.1,CIS.1.2,CIS.1.3,CIS.1.4,CIS.1.5,CIS.1.6,CIS.1.7,CIS.1.8,CIS.1.9,CIS.1.10,CIS.1.11,CIS.1.12'\
                   ',CIS.1.13,CIS.1.14,CIS.1.16,CIS.1.20,CIS.1.22,CIS.2.4,CIS.2.5,CIS.2.7,CIS.3.1,CIS.3.2,CIS.3.3,'\
                   'CIS.3.4,CIS.3.5,CIS.3.6,CIS.3.7,CIS.3.8,CIS.3.9,CIS.3.10,CIS.3.11,CIS.3.12,CIS.3.13,CIS.3.14'
    disabled_list = [disable.strip() for disable in disabled.split(",")]

    return disabled_list


def get_cis_control_list(profile, region, disable_control_list):
    boto3.setup_default_session(profile_name=profile)
    sh_client = boto3.client('securityhub', region_name=region)
    enabled_standards = sh_client.get_enabled_standards()['StandardsSubscriptions']
    for enabled_standard in enabled_standards:
        if 'cis-aws-foundations-benchmark' in enabled_standard['StandardsSubscriptionArn']:
            arn = enabled_standard['StandardsSubscriptionArn']
    controls = sh_client.describe_standards_controls(StandardsSubscriptionArn=arn)['Controls']
    control_list = []
    for control in controls:
        if control['ControlId'] in disable_control_list:
            # print(control)
            control_list.append(control['StandardsControlArn'])

    return control_list


def disable_control(profile, control):
    boto3.setup_default_session(profile_name=profile)
    sh_client = boto3.client('securityhub', region_name=region)
    control_disabled = sh_client.update_standards_control(
        StandardsControlArn=control,
        ControlStatus='DISABLED',
        DisabledReason='Disabled per AWS Guidance'
    )
    return control_disabled


def enable_control(control):
    boto3.setup_default_session(profile_name=profile)
    sh_client = boto3.client('securityhub', region_name=region)
    control_enabled = sh_client.update_standards_control(
        StandardsControlArn=control,
        ControlStatus='ENABLED'
    )
    return control_enabled


if __name__ == '__main__':
    # member_profiles = get_member_profiles()
    # regions = get_regions()
    # disable_control_list = get_controls_to_disable()
    # for member_profile in member_profiles:
    #     for region in regions:
    #         control_list = get_cis_control_list(member_profile, region, disable_control_list)
    #         for control in control_list:
    #             disable_control(member_profile, control)
    pprint(get_controls_to_disable())
