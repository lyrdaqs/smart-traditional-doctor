from pymongo import MongoClient, DESCENDING


class MongoConnection:
    def __init__(self, db_name):
        client = MongoClient('mongodb://localhost:27017/')
        self.db = client[db_name]
        
    def get_unique_id(self, collection):
        latest_item = collection.find_one(sort=[("_id", -1)])
        latest_id = latest_item["_id"] if latest_item else 0
        return latest_id + 1
    
    
    def create_user(self, user_dict):
        inserted_id = self.db.users.insert_one(user_dict).inserted_id
        return inserted_id 
    
    def get_user(self, username):
        user = self.db.users.find_one({"username": username})
        return user 
    
    def update_user(self, username, user_update):
        user = self.db.users.find_one({"username": username})
        if not user:
            return None
        updated_data = user_update.dict()
        self.db.users.update_one({"username": username}, {"$set": updated_data})
        user = self.db.users.find_one({"username": username})
        return user
    
    
    def create_fruit(self, fruit_dict):
        _id = self.get_unique_id(self.db.fruits)
        fruit_dict['_id'] = _id
        inserted_id = self.db.fruits.insert_one(fruit_dict).inserted_id
        return inserted_id 
    
    def update_fruit(self, fruit_id, fruit_update):
        fruit = self.db.fruits.find_one({"_id": fruit_id})
        if not fruit:
            return None
        updated_data = fruit_update.dict()
        self.db.fruits.update_one({"_id": fruit_id}, {"$set": updated_data})
        fruit = self.db.fruits.find_one({"_id": fruit_id})
        return fruit
    
    def delete_fruit(self, fruit_id):
        fruit = self.db.fruits.find_one({"_id": fruit_id})
        if not fruit:
            return None
        self.db.fruits.delete_one({"_id": fruit_id})
        return True
    
    
    def get_all_fruits(self):
        fields_to_retrieve = {'_id': 1, 'title': 1, 'img': 1, 'datetime': 1, 'description': 1}
        fruits_obj = self.db.fruits.find({}, fields_to_retrieve).sort("_id", DESCENDING)
        fruits = [fruit for fruit in fruits_obj]
        return fruits 
    
    def get_fruit(self, fruit_id):
        fields_to_retrieve = {'_id': 1, 'title': 1, 'img_detail': 1,
                              'img_detail_items': 1, 'datetime': 1, 'entry_content': 1,
                              'comments': 1, 'tags': 1, 'description': 1, 'img': 1}
        fruit_obj = self.db.fruits.find_one({'_id': fruit_id}, fields_to_retrieve)
        return fruit_obj
    
    def add_comment_fruit(self, fruit_id, comment):
        self.db.fruits.update_one({"_id":fruit_id}, {"$push": {"comments": comment}})
    
    
    def get_all_medicines(self):
        fields_to_retrieve = {'_id': 1, 'title': 1, 'img': 1, 'usefor': 1, 'temperament': 1}
        medicines_obj = self.db.medicines.find({}, fields_to_retrieve)
        medicines = [medicine for medicine in medicines_obj]
        return medicines 
    
    def get_medicine(self, medicine_id):
        fields_to_retrieve = {'_id': 1, 'title': 1, 'img': 1, 'entry_content': 1, 'comments': 1}
        medicine_obj = self.db.medicines.find_one({'_id': medicine_id}, fields_to_retrieve)
        return medicine_obj
    
    def add_comment_medicine(self, medicine_id, comment):
        self.db.medicines.update_one({"_id":medicine_id}, {"$push": {"comments": comment}})
        
    
    def get_illnes(self, illnes_id):
        fields_to_retrieve = {'_id': 1, 'title': 1, 'img_detail': 1,
                              'img_detail_items': 1, 'datetime': 1, 'entry_content': 1,
                              'comments': 1, 'tags': 1}
        illnes_obj = self.db.illness.find_one({'_id': illnes_id}, fields_to_retrieve)
        return illnes_obj
    
    def get_illness_by_page(self, page):
        illnes_pages = self.db.illnes_pages.aggregate([
            {
                "$match": {
                    "_id": page
                }
            },
            {
                "$lookup": {
                    "from": 'illness',
                    "localField": 'post_ids',
                    "foreignField": '_id',
                    "as": 'posts'
                }
            },
            {
                "$project": {
                    "_id": 1,
                    "posts": {
                        "_id": 1,
                        "title": 1,
                        "img": 1,
                        "datetime": 1,
                        "description": 1
                    }
                }
            }
        ]) 
        illnes_page = [illnes_page for illnes_page in illnes_pages]
        return illnes_page[0]
    
    def add_comment_illnes(self, illnes_id, comment):
        self.db.illness.update_one({"_id":illnes_id}, {"$push": {"comments": comment}})
    
    
    def get_trad_post(self, post_id):
        fields_to_retrieve = {'_id': 1, 'title': 1, 'img_detail': 1,
                        'img_detail_items': 1, 'datetime': 1, 'entry_content': 1,
                        'comments': 1, 'tags': 1}
        post_obj = self.db.traditional_posts.find_one({'_id': post_id}, fields_to_retrieve)
        return post_obj  
    
    def get_posts_by_page(self, page):
        traditional_pages = self.db.traditional_pages.aggregate([
            {
                "$match": {
                    "_id": page
                }
            },
            {
                "$lookup": {
                    "from": 'traditional_posts',
                    "localField": 'post_ids',
                    "foreignField": '_id',
                    "as": 'posts'
                }
            },
            {
                "$project": {
                    "_id": 1,
                    "posts": {
                        "_id": 1,
                        "title": 1,
                        "img": 1,
                        "datetime": 1,
                        "description": 1
                    }
                }
            }
        ]) 
        traditional_page = [traditional_page for traditional_page in traditional_pages]
        return traditional_page[0]
    
    def add_comment_post(self, post_id, comment):
        self.db.traditional_posts.update_one({"_id":post_id}, {"$push": {"comments": comment}})