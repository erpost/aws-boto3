import boto3
import configparser
import os
import datetime


def get_profiles():
    profiles = boto3.session.Session().available_profiles
    personal_profile = 'core-gov'
    profile_list = []
    for profile in profiles:
        if profile != personal_profile:
            profile_list.append(profile)

    return profile_list


def get_aws_account_id(profile):
    boto3.setup_default_session(profile_name=profile)
    client = boto3.client("sts")

    return client.get_caller_identity()["Account"]


def get_aws_account_alias(profile):
    boto3.setup_default_session(profile_name=profile)
    iam = boto3.client('iam')

    return iam.list_account_aliases()['AccountAliases'][0]


def get_current_user(profile):
    boto3.setup_default_session(profile_name=profile)
    iam = boto3.client('iam')
    username = iam.get_user()["User"]["UserName"]

    return username


def get_current_access_key_id(profile):
    session = boto3.Session(profile_name=profile)
    credentials = session.get_credentials()
    current_credentials = credentials.get_frozen_credentials()

    return current_credentials.access_key  # Also: current_credentials.secret_key and current_credentials.token


def get_user_access_keys(user, profile):
    keys = []
    boto3.setup_default_session(profile_name=profile)
    iam_client = boto3.client('iam')
    access_keys = iam_client.list_access_keys(UserName=user)['AccessKeyMetadata']
    for access_key in access_keys:
        keys.append(access_key['AccessKeyId'])

    return keys


def get_access_key_age(user, profile):
    current_date = datetime.date.today()
    boto3.setup_default_session(profile_name=profile)
    iam_client = boto3.client('iam')
    access_keys = iam_client.list_access_keys(UserName=user)['AccessKeyMetadata']
    for access_key in access_keys:
        createdate = access_key['CreateDate']

    keyage = current_date - createdate.date()

    return keyage.days


def delete_unused_access_key(user, profile, current_key):
    iam = boto3.client('iam')
    deleted_key = None

    for access_key in get_user_access_keys(user, profile):
        if access_key != current_key:
            deleted_key = access_key
            iam.delete_access_key(
                AccessKeyId=access_key,
                UserName=user
            )

    return deleted_key


def create_access_key(user, profile):
    boto3.setup_default_session(profile_name=profile)
    iam = boto3.client('iam')
    key = iam.create_access_key(UserName=user)

    return {'aws_access_key_id': key['AccessKey']['AccessKeyId'],
            'aws_secret_access_key': key['AccessKey']['SecretAccessKey']}


def write_access_key_to_file(user, profile, key_dict):
    config = configparser.ConfigParser()
    credentials_file = os.path.expanduser('~/.aws/credentials')
    if os.path.exists(credentials_file):
        config.read(credentials_file)

    # Add the new credentials
    config[profile] = key_dict

    # Write the updated credentials file
    with open(credentials_file, 'w') as f:
        config.write(f)


if __name__ == "__main__":

    for profile in get_profiles():
        user = get_current_user(profile)
        current_key = get_current_access_key_id(profile)
        print('AWS Account: ', get_aws_account_id(profile))
        print('AWS Alias: ', get_aws_account_alias(profile))
        print('Current User: ', user)
        print('Access Keys:', get_user_access_keys(user, profile))
        print('Deleting Unused Access Key (if any): ', delete_unused_access_key(user, profile, current_key))
        key_age = get_access_key_age(user, profile)
        print('Current Key Age: ', key_age)
        if key_age > 1:
            print('Rotating Keys...\n')
            new_key = create_access_key(user, profile)
            print('New Keys: ', new_key)
            write_access_key_to_file(user, profile, new_key)
        else:
            print('Skipping Rotation...\n')
