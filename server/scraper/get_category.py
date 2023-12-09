import requests
from bs4 import BeautifulSoup
import os
from pymongo import MongoClient



client = MongoClient('mongodb://localhost:27017/')
db = client['TraditionalMedicine']


def download_image(img_url):
    image_response = requests.get("https:" + img_url)
    if image_response.status_code == 200:
        img_name = os.path.basename(img_url)
        save_path = os.path.join("images", img_name) 
        with open(save_path, 'wb') as img_file:
            img_file.write(image_response.content)
        print(f"Image '{img_name}' saved successfully.")
    else:
        print("Failed to retrieve the image")


def get_parser(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
    else:
        print("Failed to retrieve the webpage")
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup


def generate_unique_id():
    sequence_doc = db.traditional_posts.find_one_and_update(
        {'_id': 'custom_id'},
        {'$inc': {'seq': 1}},
        return_document=True
    )
    return sequence_doc['seq'] % 10000 


counter = 0
for page in range(1, 100):
    print(page)
    url = ""
    if page == 1:
        url = "https://irismed.ir/category/traditional-medicine/"
    else:
        url = f"https://irismed.ir/category/traditional-medicine/page/{page}/"
    soup = get_parser(url)

    li_posts = soup.find('ul', id='posts-container').find_all('li', class_='post-item')

    for li_post in li_posts:
        counter += 1
        details_div = li_post.find('div', class_='post-details')
        detail_link = details_div.find('h2', class_='post-title').find('a').get("href")
        dsoup = get_parser(detail_link)
        a_cats = dsoup.find('div', class_='entry-header').find_all('a', class_='post-cat')
        categories = [a_cat.text for a_cat in a_cats]
        db.traditional_posts.update_one({"_id": counter}, {"$set": {"tags": categories}})
        print(categories)
        
