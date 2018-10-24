import boto3


def list_buckets():
    boto3.setup_default_session()
    s3 = boto3.resource('s3')

    return s3.buckets.all()


if __name__ == '__main__':
    buckets = list_buckets()
    count = 0
    for bucket in buckets:
        print(bucket.name)
        count += 1

    print('\n{} buckets total'.format(count))
