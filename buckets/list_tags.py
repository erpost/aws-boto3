import boto3
from botocore.exceptions import ClientError
from pprint import pprint


def list_buckets():
    s3 = boto3.resource('s3')

    return s3.buckets.all()


def list_tags():
    for bucket in list_buckets():
        try:
            s3_client = boto3.client('s3')
            response = s3_client.get_bucket_tagging(Bucket=bucket.name)
            pprint(response)

        except ClientError as err:
            if err.response['Error']['Code'] == 'NoSuchTagSet':
                print('No Tags: {}'.format(err.response['Error']['BucketName']))
            else:
                print('Unknown Error: {}'.format(err.response))


if __name__ == '__main__':
    # aws_buckets = list_buckets()
    # for aws_bucket in aws_buckets:
    #     print(aws_bucket.name)
    list_tags()
