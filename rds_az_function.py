import csv

def get_db_instances(rds_client):
    response = rds_client.describe_db_instances()
    return response            

def csv_create (filename, instance):
    fieldnames = ['DBInstance','Engine','MultiAZ']
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in instance['DBInstances']:
            identi = i['DBInstanceIdentifier']
            engi = i['Engine']
            az = str(i['MultiAZ'])
            writer.writerow({'DBInstance':identi,'Engine':engi,'MultiAZ':az})

