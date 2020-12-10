import requests
from bs4 import BeautifulSoup
import csv

File = 'Parsed_autoria.csv'
URL = 'https://auto.ria.com/uk/newauto/marka-mercedes-benz/'
HEADERS = {'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (HTML, like Gecko)"
                         " Chrome/87.0.4280.88 Safari/537.36",
           "accept": "*/*"}


def save_csv(cars, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(['title', 'link', 'price', 'city'])
        for i in cars:
            writer.writerow([i['title'], i['link'], i['price'], i['city']])


def get_html(params=None):
    return requests.get(URL, headers=HEADERS, params=params)


def get_pages(html):
    soup = BeautifulSoup(html, "html.parser")
    pages = soup.find_all('span', class_='page-item mhide')
    return int(pages[-1].get_text()) if pages else 1


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_='proposition')
    cars = []
    for item in items:
        cars.append({
            "title": item.find('h3', class_='proposition_name').get_text(strip=True),
            "link": f"{URL[:-20]}{item.find('a').get('href')}",
            "price": item.find('span', class_="green bold size18").get_text(strip=True),
            'city': item.find('div', class_="proposition_region").strong.get_text(strip=True)
        })
    return cars


def parse():
    html = get_html()
    if html.status_code == 200:
        cars = []
        for p in range(1, get_pages(html.text) + 1):
            print(f'Parsing page: {p}')
            html = get_html(params={'page': p})
            get_content(html.text)
            cars.extend(get_content(html.text))
        print(f'Count {len(cars)}')
        save_csv(cars, File)
    else:
        print('Error')


parse()
