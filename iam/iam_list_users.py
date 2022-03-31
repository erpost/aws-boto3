from pprint import pprint
import boto3


def list_iam_users():
    iam = boto3.client('iam')

    return iam.list_users()


if __name__ == '__main__':
    pprint(list_iam_users())
    # for user in list_iam_users()['Users']:
    #     print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
    #         user['UserName'],
    #         user['UserId'],
    #         user['Arn'],
    #         user['CreateDate']
    #         )
    #     )





