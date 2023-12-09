from elasticsearch import Elasticsearch


class ElasticSearchConnection:
    def __init__(self, index):
        self.es = Elasticsearch(hosts=['http://localhost:9200'])
        self.index = index
        
        
    def get_tag_items(self, tag):
        query = {
            "_source": ["title", "img", "description", "store_id", "role"],
            "query": {
                "term":{
                    "tags.keyword": tag
                }
            }
        }
        result = self.es.search(index=self.index, body=query, request_timeout=6000)
        search_list = [item['_source'] for item in result['hits']['hits']]
        return search_list
    
    
    def search_items(self, keyword):
        query = {
            "_source": ["title", "img", "description", "store_id", "role"],
            "query": {
                "multi_match": {
                    "query": keyword,
                    "fields": ["title^4", "tags.keyword^2", "description^3", "entry_content"],
                    "type": "best_fields"
                }
            }
        }
        result = self.es.search(index=self.index, body=query, request_timeout=6000)
        search_list = [item['_source'] for item in result['hits']['hits']]
        return search_list
    
    
    def search_questions(self, keyword):
        query = {
            "_source": ["text"],
            "query": {
                "multi_match": {
                    "query": keyword,
                    "fields": ["text"],
                    "type": "best_fields"
                }
            }
        }
        result = self.es.search(index=self.index, body=query, request_timeout=6000)
        search_list = [item['_source'] for item in result['hits']['hits']]
        return search_list

