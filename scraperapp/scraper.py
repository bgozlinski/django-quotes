import requests
from bs4 import BeautifulSoup


def scraper():
    if requests.method == 'POST':
        url = 'http://52.90.218.108:8000/'
        response = requests.post(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)

