import requests
from bs4 import BeautifulSoup
import csv
from config import agent


def get_html(url):
    user_agent = agent
    r = requests.get(url, headers=user_agent)
    if r.ok:
        return r.text


def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow([data['vacancy_name'],
                        data['link'],
                        data['company_name']])


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    advs = soup.find_all('div', class_='vacancy-serp-item')

    for adv in advs:
        vacancy_name = adv.find('a', class_='bloko-link HH-LinkModifier').text.strip()
        company_name = adv.find('a', class_='bloko-link bloko-link_secondary').text.strip()
        link = adv.find('a', class_='bloko-link HH-LinkModifier').get('href')

        data = {'vacancy_name': vacancy_name,
                'link': link,
                'company_name': company_name}
        write_csv(data)


def main():
    page = 0
    while True:
        # search_period=7 - последняя неделя; text=Data - запрос
        url = 'https://hh.ru/search/vacancy?L_is_autosearch=false&clusters=true&enable_snippets=true&search_period=7&text=Data&page={}'.format(page)
        page = page + 1
        get_page_data(get_html(url))
    print('Done!')


if __name__ == '__main__':
    main()
