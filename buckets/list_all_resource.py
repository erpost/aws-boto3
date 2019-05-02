import boto3


profile = 'jau-sec-admin'
region = 'us-east-1'


def list_buckets():
    boto3.setup_default_session(profile_name=profile)
    s3 = boto3.resource('s3', region_name=region)

    return s3.buckets.all()


if __name__ == '__main__':
    buckets = list_buckets()
    print(buckets)
    count = 0
    for bucket in buckets:
        print(bucket.name)
        count += 1

    print('\n{} buckets total'.format(count))
