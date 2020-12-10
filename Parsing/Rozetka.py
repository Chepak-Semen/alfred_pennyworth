from bs4 import BeautifulSoup
import requests
import json

URL ='https://rozetka.com.ua/notebooks/c80004/'
HEADER = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', "accept": "*/*"}

class Error(Exception):
    pass
        

def get_html(url):
    return requests.get(url, headers=HEADER)

def check_conect(html):
    return True if html.status_code == 200 else False

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('li', class_='catalog-grid__cell catalog-grid__cell_type_slim')
    data = []
    for item in items:
        data.append({
            'title': item.find('span', class_='goods-tile__title').get_text(strip=True),
            "price": int(str(item.find('span', class_='goods-tile__price-value').get_text(strip=True)).replace('\xa0', ''))
            })
    return sorted(data, key=lambda x: x['price'])



def write_json(a):
    with open('Rozetka_parsed.json', 'w', encoding="utf-8") as file:
        json.dump(a, file, indent=4, ensure_ascii=False)



def parse():
    html = get_html(URL)
    try: 
        check_conect(html)
        data = get_content(html=html.text)
        write_json(a=data)
    except Error:
        print('Error')

        


parse()