import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants
from azure.cosmos.partition_key import PartitionKey

import os
url = 
key = 
client = cosmos_client.CosmosClient(url, {'masterKey': key})

database = client.get_database_client('amazon-jobs')

container_definition = {
    'id': 'indeed_jobs',
    'partitionKey': {
        'paths': ['/job_id']
    }
}

container = database.create_container_if_not_exists(
    id='indeed', 
    partition_key=PartitionKey(path="/id"),
    offer_throughput=400
)

database_id = 'amazon-jobs'
container_id= 'indeed'

container_client = database.get_container_client(container_id)

for i in range(1, 10):
    container_client.upsert_item({
            'id': 'item{0}'.format(i),
            'productName': 'Widget',
            'productModel': 'Model {0}'.format(i)
        }
    )