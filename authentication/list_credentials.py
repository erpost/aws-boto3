import configparser
import os

key_file = os.path.expanduser('~/.aws/credentials')

parser = configparser.ConfigParser()
parser.read(key_file)

for sect in parser.sections():
    print('Section:', sect)
    for k,v in parser.items(sect):
        print('{} = {}'.format(k, v))
    print()
