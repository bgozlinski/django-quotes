from dotenv import load_dotenv
from mongoengine import connect, disconnect
from quotes.settings import dotenv_path
import os


class MongoDBConnection:
    def __init__(self):
        load_dotenv(dotenv_path=dotenv_path)
        self.db_name = os.getenv('MONGODB_NAME')
        self.host = os.getenv('MONGODB_HOST')
        self.username = os.getenv('MONGODB_USERNAME')
        self.password = os.getenv('MONGODB_PASSWORD')

    def open_connection(self):
        connect(
            db=self.db_name,
            host=self.host,
            username=self.username,
            password=self.password
        )

    def close_connection(self):
        disconnect()
        print("Disconnected from MongoDB.")
