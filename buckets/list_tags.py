import boto3
from botocore.exceptions import ClientError


def list_buckets():
    s3 = boto3.resource('s3')

    return s3.buckets.all()


def list_tags():
    for bucket in list_buckets():
        try:
            s3_client = boto3.client('s3')
            response = s3_client.get_bucket_tagging(Bucket=bucket.name)
            tag_dict = {}
            print('#' * 25)
            print('Bucket: ', bucket.name)
            tag_set = response['TagSet']
            for tags in tag_set:
                tag_dict[tags['Key']] = tags['Value']
            print(tag_dict)

        except ClientError as err:
            if err.response['Error']['Code'] == 'NoSuchTagSet':
                print('#' * 25)
                print('Bucket: {}'.format(err.response['Error']['BucketName']))
                print('No Tags')
            else:
                print('Unknown Error: {}'.format(err.response))

    print('#' * 25)


if __name__ == '__main__':
    list_tags()
