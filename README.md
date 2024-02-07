# Quotes Scraper Project

This project is designed to replicate https://quotes.toscrape.com/ to store quotes. There is option to scrap data
from a web page and save them on MongoDB database. It utilizes Django and Postgres database for the backend, 
BeautifulSoup for scraping, MongoEngine for MongoDB interactions.

## Features

- Add authors and quotes.
- Store data on Postgres database.
- Create new Users via Sign-up forms.
- Scrape quotes and their authors from a site.
- Save scraped data to MongoDB with.
- Pagination support to scrape data across multiple pages.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.11+
- Django
- Requests and BeautifulSoup for scraping
- psycopg2 for Postgres interactions
- mongoengine for MongoDB interactions

## Installation

Clone the project repository:

```bash
git clone https://github.com/bgozlinski/django-quotes.git
cd django-quotes
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Configuration

### Environment Variables

For security reasons, it's recommended to use environment variables for sensitive information like database credentials:
For more view visit [.env Template](.env.dist)

## Usage

To start scraping quotes, run the Django server:

```bash
python manage.py runserver
```

Navigate to the scraper's URL (e.g., `http://127.0.0.1:8000/scraper/`) or click the "Scrap" button to begin scraping.


## License

This project is licensed under the [MIT License](LICENSE).
