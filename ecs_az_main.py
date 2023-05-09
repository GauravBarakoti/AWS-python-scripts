from ecs_az_function import get_function, client, csv_create

ecs = client()
cluster_statuses = get_function(ecs)
csv_create(cluster_statuses)
