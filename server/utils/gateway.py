#from ai.mysql_connection import MySqlConnection
from db.mongo_connection import MongoConnection
from db.elastic_connection import ElasticSearchConnection
import redis


mongo_conn = MongoConnection("TraditionalMedicine")
el_conn = ElasticSearchConnection("health_items")
el_con_qa = ElasticSearchConnection("question_awnsering")
r = redis.Redis(host='localhost', port=6379, db=0)
#mysql = MySqlConnection()
AI_DOCKER_SERVICE = "http://127.0.0.1:8001"

