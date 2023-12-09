import requests
from bs4 import BeautifulSoup
import os
from pymongo import MongoClient



client = MongoClient('mongodb://localhost:27017/')
db = client['TraditionalMedicine']
db.fruits.insert_one({'_id': 'custom_id', 'seq': 0})


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
    sequence_doc = db.fruits.find_one_and_update(
        {'_id': 'custom_id'},
        {'$inc': {'seq': 1}},
        return_document=True
    )
    return sequence_doc['seq'] % 10000 


soup = get_parser("https://irismed.ir/category/pharmaceutical-formulations/fruits/")

li_posts = soup.find('ul', id='posts-container').find_all('li', class_='post-item')

for li_post in li_posts:
    img_url = li_post.find('a', class_='post-thumb').find("img").get('data-src')
    #download_image(img_url)
    details_div = li_post.find('div', class_='post-details')
    pdatetime = details_div.find('div', class_='post-meta').find('span', class_='date').text
    title = details_div.find('h2', class_='post-title').find('a').text
    description = details_div.find('p', class_='post-excerpt').text
    detail_link = details_div.find('h2', class_='post-title').find('a').get("href")
    dsoup = get_parser(detail_link)
    article = dsoup.find('article', id='the-post')
    img_url_detail = article.find('figure', class_='single-featured-image').find("img").get('data-src')
    #download_image(img_url_detail)
    entry_content = article.find('div', class_='entry-content')
    imgs_entry = entry_content.find_all('img')
    
    img_detail_items = []
    for img_entry in imgs_entry:
        try:
            img_url_detail_c = img_entry.get("data-src")
            img_detail_items.append(img_url_detail_c.split('/')[-1])
            #download_image(img_url_detail_c)
        except:
            pass
    [div_img.extract() for div_img in entry_content.find_all('figure')]
    [div_img.extract() for div_img in entry_content.find_all('img')]
    entry_content.find("div", class_="post-bottom-meta").extract()

    fruit = {
        '_id': generate_unique_id(),
        'title': title,
        'img': img_url.split('/')[-1],
        'img_detail': img_url_detail.split('/')[-1],
        'img_detail_items': img_detail_items,
        'datetime': pdatetime,
        'description': description,
        'entry_content': str(entry_content)
    }
    inserted_id = db.fruits.insert_one(fruit).inserted_id
    print(f'{inserted_id} inserted in db')
