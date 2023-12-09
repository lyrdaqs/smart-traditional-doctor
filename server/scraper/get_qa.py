import requests
from bs4 import BeautifulSoup
import os, json


for page in range(1, 100):
    print(page)
    url = f"http://www.irantebesonati.ir/faq/list/{page}/"
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
    else:
        print("Failed to retrieve the webpage")
    soup = BeautifulSoup(html_content, 'html.parser')

    qa_elements = soup.find('div', id="content").find_all('p', class_="normaltext")

    page_data = []
    for qa_el in qa_elements[1:]:
        for br in qa_el.find_all('br'):
            br.replace_with('')
        
        span = qa_el.find_all('span', style="color:#fff;")
        span[0].string = "سوال:\n"
        span[1].string = "\nپاسخ:\n"
            
        qa_text = qa_el.text.strip()
        lines = qa_text.split('\n')
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        cleaned_text = '\n'.join(cleaned_lines)
        page_data.append({ "text": cleaned_text })

    headers = {'Content-type': 'application/json'}
    response = requests.post("http://localhost:8081", data=json.dumps(page_data), headers=headers)
    
    
    
