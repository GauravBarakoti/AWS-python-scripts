import boto3
import csv

rds_ob = boto3.client('rds')

response = rds_ob.describe_db_instances()

with open ('list.csv','w',newline='') as csvfile:
    fieldnames = ['DBInstance','Engine','MultiAZ']
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    thewriter.writeheader()

    for i in response['DBInstances']:
        # print('DBInstanceIdentifier: ' + i['DBInstanceIdentifier'])
        # print('Engine: ' + i['Engine'])
        # print('MultiAZ: ' + str(i['MultiAZ']))
        identi = i['DBInstanceIdentifier']
        engi = i['Engine']
        az = str(i['MultiAZ'])
        thewriter.writerow({'DBInstance':identi,'Engine':engi,'MultiAZ':az})
        