import boto3

profile = ''

boto3.setup_default_session(profile_name=profile)
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)
