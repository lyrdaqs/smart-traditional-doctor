import requests
from bs4 import BeautifulSoup
import os
from pymongo import MongoClient
import base64


client = MongoClient('mongodb://localhost:27017/')
db = client['TraditionalMedicine']
db.medicines.insert_one({'_id': 'custom_id', 'seq': 0})


def download_image(img_url):
    image_response = requests.get(img_url)
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
    sequence_doc = db.medicines.find_one_and_update(
        {'_id': 'custom_id'},
        {'$inc': {'seq': 1}},
        return_document=True
    )
    return sequence_doc['seq'] % 10000 


soup = get_parser("https://tabaye.ir/herbal-temper-list/")

table_posts = soup.find_all('table', class_='mgh_table_multicolor')[0]

tr_list = table_posts.find('tbody').find_all('tr')[1:]

for tr in tr_list:
    try:
        td_list = tr.find_all('td')
        link = td_list[0].find('a').get('href')
        title = td_list[0].text
        temperament = td_list[1].text
        usefor = td_list[2].text
        dsoup = get_parser(link)
        detail_main = dsoup.find('main', id='main')
        img_url = detail_main.find('div', class_='post-thumbnail').find('img').get('data-src')
        download_image(img_url)
        entry_content = detail_main.find('div', class_='entry-content')
        [div_img.extract() for div_img in entry_content.find_all('img')]
        entry_content.find('div', class_='lwptoc-baseItems').extract()
        entry_content.find('div', class_='su-box').extract()
        entry_content.find('div', class_='pix-post-meta-box').extract()
        medicine = {
            '_id': generate_unique_id(),
            'title': title,
            'temperament': temperament,
            'usefor': usefor,
            'img': img_url.split('/')[-1],
            'entry_content': str(entry_content)
        }
        inserted_id = db.medicines.insert_one(medicine).inserted_id
        print(f'{inserted_id} inserted in db')
    except:
        print(tr)
    

