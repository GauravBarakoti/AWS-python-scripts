from client import create_rds_client

from logic import get_db_instances

rds_client = create_rds_client()
db_instances = get_db_instances(rds_client, 'list.csv')
# save_to_csv(db_instances, )
