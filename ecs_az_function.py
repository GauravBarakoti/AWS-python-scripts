import boto3
import csv

def client():
    # Set up the ECS client
    client = boto3.client('sts')
    assumed_role_object = client.assume_role(
        RoleArn='arn:aws:iam::621641769616:role/rds_read',
        RoleSessionName='rds_read',
    )
    credentials = assumed_role_object['Credentials']
    ecs = boto3.client(
        'ecs',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'],
    )
    return ecs


def get_function(ecs):
    clusters = ecs.list_clusters()['clusterArns']
    cluster_statuses = []
    for cluster_arn in clusters:
        cluster_name = cluster_arn.split("/")[-1]
        services = ecs.list_services(cluster=cluster_name)['serviceArns']
        az_set = set()        
        for service_arn in services:
            service_name = service_arn.split("/")[-1]
            tasks = ecs.list_tasks(cluster=cluster_name, serviceName=service_name)['taskArns']            
            for task_arn in tasks:
                task_details = ecs.describe_tasks(cluster=cluster_name, tasks=[task_arn])['tasks'][0]
                print(task_details['availabilityZone'])
                # print(task_arn_az['availabilityZone'])
                az_set.add(task_details['availabilityZone'])
        
        if len(az_set) == 1:
            status = "Yellow"
        else:
            status = "Green"
        
        cluster_statuses.append([cluster_name, status])
    return cluster_statuses


def csv_create(cluster_statuses):
    with open('ecs_cluster_statuses.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Cluster Name', 'Status'])
        for row in cluster_statuses:
            writer.writerow(row)

