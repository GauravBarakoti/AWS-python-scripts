import boto3

def create_rds_client():
    # rds_ob = boto3.client('rds')
    # return rds_ob


    client = boto3.client('sts')
    assumed_role_object = client.assume_role(
        RoleArn='arn:aws:iam::621641769616:role/rds_read',
        RoleSessionName='rds_read',
    )
    credentials = assumed_role_object['Credentials']

    rds_client = boto3.client(
        'rds',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'],
    )

    return rds_client
