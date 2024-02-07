from scraperapp.db.connect_db import MongoDBConnection
from scraperapp.db.models import Quote

def upload_data_to_mongodb(data):
    db_connection = MongoDBConnection()
    db_connection.open_connection()

    for quote_data in data:
        quote = Quote(quote=quote_data['quote'], author=quote_data['author'])
        quote.save()
