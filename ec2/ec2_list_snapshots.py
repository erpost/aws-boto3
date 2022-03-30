from pprint import pprint
import boto3


def list_snapshots():
    ecc = boto3.client('ec2')

    return ecc.describe_snapshots()


if __name__ == '__main__':
    snaps = list_snapshots()
    f = open("snap.txt", "w")
    # f.write(str(snaps))
    # print(type(snaps))
    snapshots = snaps['Snapshots']
    for snapshot in snapshots:
        print(snapshot, '\n')
        f.write(str(snapshot))
        f.write('\n')
