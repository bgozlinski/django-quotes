from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

from scraperapp.db.seed import upload_data_to_mongodb


# Create your views here.
def scraper(request):
    print('Scraping quotes...')

    base_url = 'http://127.0.0.1:8000/'
    page = 1
    quotes_data = []

    while True:
        print(f'Scraping page {page}')
        url = f"{base_url}?page={page}"
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        quotes = soup.find_all("div", class_="card mb-3")  # Adjust based on actual structure

        if not quotes:
            break  # Stop if there are no quotes on the page

        for quote in quotes:
            # Extract quote text and author, adjust selectors as needed
            text = quote.find("p").get_text(strip=True)  # Example, adjust as needed
            author = quote.find("footer").get_text(strip=True)  # Example, adjust as needed
            quotes_data.append({"quote": text, "author": author})

        # Check if there's a next page. If there's no "Next" button, stop.
        next_page = soup.find("a", class_="page-link next")
        if next_page and next_page.get('href'):
            page += 1
        else:
            break

    upload_data_to_mongodb(quotes_data)

    return HttpResponse("Data scraped and processed.")
