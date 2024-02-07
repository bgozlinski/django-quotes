from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.
@ensure_csrf_cookie
def scraper(request):
    print('Scraping quotes...')
    if request.method == 'POST':
        url = 'http://127.0.0.1:8000/'
        response = requests.post(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)

        return redirect(to='quoteapp:main')

    return redirect(to='quoteapp:main')




