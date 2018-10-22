import boto3


def list_buckets(profile):
    boto3.setup_default_session(profile_name=profile)
    s3 = boto3.resource('s3')

    return s3.buckets.all()


if __name__ == '__main__':
    aws_profile = input('What profile are you using: ')

    for bucket in list_buckets(aws_profile):
        print(bucket.name)
