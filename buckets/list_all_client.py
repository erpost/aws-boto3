from pprint import pprint
import boto3


profile = 'jau-sec-admin'
region = 'us-east-1'


def list_buckets():
    boto3.setup_default_session(profile_name=profile)
    s3 = boto3.client('s3', region_name=region)

    return s3.list_buckets()


if __name__ == '__main__':
    buckets = list_buckets()
    print(type(buckets))
    pprint(buckets)
    for bucket in buckets['Buckets']:
        print(f'{bucket["Name"]}')
