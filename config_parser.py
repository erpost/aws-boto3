import configparser
import os


config = configparser.ConfigParser()
credentials_file = os.path.expanduser('~/.aws/credential-test')
if os.path.exists(credentials_file):
    config.read(credentials_file)

# Print out credentials
for profile in config.sections():
    print('#####' + profile + '#####')
    print(config[profile])
    # print(config[profile]['aws_access_key_id'])
    # print(config[profile]['aws_secret_access_key'])
    for k, v in config.items(profile):
        print(k + ': ' + v)

# Add the new credentials
config['default-1'] = {
    'aws_access_key_id': 'access-key-default-1b',
    'aws_secret_access_key': 'secret-key-default-1b'
}

# Write the updated credentials file
with open(credentials_file, 'w') as f:
    config.write(f)


