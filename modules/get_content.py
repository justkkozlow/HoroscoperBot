import requests
from bs4 import BeautifulSoup as Bs

import config

signs = [
    'Овен', 'Телец', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы'
]

def sign_list(url):
    """
    Функция обрабатывает URL-адрес, парсит имеющиеся ссылки на знаки зодиака и помещает их в словарь.
    :param url: config.URL
    :return sign_db:
    """
    signs_urls = []

    r = requests.get(url)
    soup = Bs(r.text, 'html.parser')
    links = soup.find_all('a',
                          class_='p-imaged-item p-imaged-item_circle p-imaged-item_rune p-imaged-item_shadow_inner')
    for i in links:
        urls_list = f'{url}{i["href"]}'
        signs_urls.append(urls_list)

    sign_db = dict(zip(signs, signs_urls))
    return sign_db


def content(callback):
    r = requests.get(sign_list(config.URL).setdefault(callback.data))
    soup = Bs(r.text, 'html.parser')
    selected_sign = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    return [s.text for s in selected_sign]
