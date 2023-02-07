import requests
from bs4 import BeautifulSoup as Bs

from sign_db import *


def start_content(url):
    r = requests.get(url)
    soup = Bs(r.text, 'html.parser')
    selected_sign = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    return [s.text for s in selected_sign]


def content(callback):
    r = requests.get(sign_list.setdefault(callback.data))
    soup = Bs(r.text, 'html.parser')
    selected_sign = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    return [s.text for s in selected_sign]
