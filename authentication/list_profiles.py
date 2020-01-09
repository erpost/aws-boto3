import boto3


profiles = boto3.session.Session().available_profiles
print(profiles)
