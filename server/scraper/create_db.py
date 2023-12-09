from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['TraditionalMedicine']

illnes_pages = db.illnes_pages.aggregate([
  {
    "$match": {
      "_id": 1
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
          "title": 1,
          "img": 1
      }
    }
  }
])

for illnes_page in illnes_pages:
    print(illnes_page)
