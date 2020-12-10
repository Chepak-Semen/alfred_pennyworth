import requests
from bs4 import BeautifulSoup
import csv
import argparse

File = 'Parsed_dou.csv'
HEADERS = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "accept": "*/*"}


def save_csv(cars, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter="=")
        writer.writerow(["link", 'title', 'company', 'salary', 'city'])
        for i in cars:
            writer.writerow([i["link"], i['title'], i['company'], i['salary'], i['city']])


def get_html(url, params=None):
    return requests.get(url, headers=HEADERS, params=params)


def get_pages(html):
    soup = BeautifulSoup(html, "html.parser")
    pages = soup.find_all('span', class_='page-item mhide')
    return int(pages[-1].get_text()) if pages else 1


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('li', class_='l-vacancy')
    vacancy = []

    for item in items:

        if item.find('span', class_='salary'):
            s = str(item.find('div', class_='title').span.text).replace('\xa0', ' ')
        else:
            s = "Не вказано"

        if item.find('span', class_='cities'):
            city = item.find('span', class_='cities').get_text(strip=True)
        else:
            city = "Не вказано"

        vacancy.append({
            'link': str(item.find('a', class_='vt').get('href')).replace(' ', ' '),
            "title": str(item.find('a', class_='vt').get_text(strip=True)).replace(' ', ' '),
            'company': str(item.find('a', class_='company').get_text(strip=True)).replace(' ', ' '),
            'salary': str(s),
            'city': city,
        })
    return vacancy


def parse(url):
    html = get_html(url=url)

    if html.status_code == 200:
        vacancy = []
        for p in range(1, get_pages(html.text) + 1):
            print(f'Parsing page: {p}')
            html = get_html(url=url, params={'page': p})
            get_content(html.text)
            vacancy.extend(get_content(html.text))
        print(f'Count {len(vacancy)}')
        save_csv(vacancy, File)
    else:
        print('Error')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--your_vacancy",
                        dest="your_vacancy",
                        required=True,
                        help='your_vacancy'
                        )
    arguments = parser.parse_args()

    if arguments.your_vacancy:
        link = f"https://jobs.dou.ua/vacancies/?category=Python&search={arguments.your_vacancy}&descr=1"
        parse(url=link)


if __name__ == '__main__':
    main()
