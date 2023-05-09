
from rds_az_client import create_rds_client

from rds_az_function import get_db_instances,csv_create

rds_client = create_rds_client()
values = db_instances = get_db_instances(rds_client)
# save_to_csv(db_instances, )
csv_create('new-list.csv',values)