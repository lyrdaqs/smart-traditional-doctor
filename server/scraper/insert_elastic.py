from elasticsearch import Elasticsearch
from pymongo import MongoClient
from elasticsearch.helpers import bulk


es = Elasticsearch(hosts=['http://localhost:9200'])

client = MongoClient('mongodb://localhost:27017/')
db = client['TraditionalMedicine']

projection = {
    "_id": 0,
    "store_id": "$_id",
    "title": 1,
    "description": "$usefor",
    "entry_content": 1,
    "img": 1,
    "tags": 1,
    "role": "medicine"
}
data = db.medicines.find({}, projection)

batch_data = [{"_index": "health_items", "_source":item} for item in data]
bulk(es, batch_data)