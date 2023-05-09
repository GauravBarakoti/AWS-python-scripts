import boto3,csv
from datetime import datetime
from dateutil.parser import parse

def client():
    # client_ob = boto3.client("ec2")
    # def create_rds_client():
    # rds_ob = boto3.client('ec2')
    # return rds_ob
    client = boto3.client('sts')
    assumed_role_object = client.assume_role(
        RoleArn='arn:aws:iam::977893653678:role/ec2-readonly',
        RoleSessionName='ec2-readonly',
    )
    credentials = assumed_role_object['Credentials']
    rds_client = boto3.client(
        'ec2',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'],
    )
    return rds_client

    # return client_ob


def get_old_ami_check(client_ob):
    current_date=datetime.now()
    my_ami = client_ob.describe_images(Owners=['self'])['Images']
    max_ami_age = 2
    outdated_amis = []
    for ami in my_ami:
        creation_date=ami['CreationDate']
        creation_date_parse=parse(creation_date).replace(tzinfo=None)
        ami_id = ami['ImageId']
        diff_in_days = (current_date - creation_date_parse).days
        print(diff_in_days)
        if diff_in_days > max_ami_age:
                outdated_amis.append(ami_id)
    return outdated_amis



def csv_create (outdated_ami,filename): 
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['ami-id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in outdated_ami:
            writer.writerow({'ami-id':i})