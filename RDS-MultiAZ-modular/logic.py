
import csv

def get_db_instances(rds_client,filename):
    response = rds_client.describe_db_instances()
    with open (filename,'w',newline='') as csvfile:
        fieldnames = ['DBInstance','Engine','MultiAZ']
        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        thewriter.writeheader()

        for i in response['DBInstances']:
            identi = i['DBInstanceIdentifier']
            engi = i['Engine']
            az = str(i['MultiAZ'])
            thewriter.writerow({'DBInstance':identi,'Engine':engi,'MultiAZ':az})
            

# def save_to_csv(db_instances, filename):
#     with open(filename, 'w', newline='') as csvfile:
#         fieldnames = ['DBInstance', 'Engine', 'MultiAZ']
#         thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         thewriter.writeheader()
#         for db_instance in db_instances:
#             thewriter.writerow(db_instance)
            # print(f"Data written to file: {filename}")
