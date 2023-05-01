import boto3

def create_rds_client():
    rds_ob = boto3.client('rds')
    return rds_ob