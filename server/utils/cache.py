from utils.gateway import r
import json


def cache(keyword):
    key = keyword
    if r.exists(key):
        print("HIT")
        result = r.get(key).decode()
        docs = json.loads(result)
        return docs 
    else:
        print("MISS")
        return None