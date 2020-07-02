import azure.cosmos.cosmos_client as cosmos_client
from constants import *
import csv

#client initialisation
client = cosmos_client.CosmosClient(url, {'masterKey': key})
database = client.get_database_client(database_id)
container = database.get_container_client(container_id)

items = list(container.query_items(
        query="SELECT r.title,r.company,r.rating,r.posted_date FROM indeed r WHERE r.id!=@id",
        parameters=[
            { "name":"@id", "value": "1" }
        ],
        enable_cross_partition_query=True
    ))

keys = items[0].keys()
with open('jobs.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(items)
