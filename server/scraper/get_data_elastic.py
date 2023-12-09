from elasticsearch import Elasticsearch


es = Elasticsearch(hosts=['http://localhost:9200'])

query = {
    "query": {
        "match_all":{}
    }
}


result = es.search(index="question_awnsering", body=query, request_timeout=6000)
search_list = [item['_source'] for item in result['hits']['hits']]

print(search_list)