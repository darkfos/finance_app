from pymongo import MongoClient
from src.settings.db_settings import DatabaseSettings


class MongoEngine:
    def __init__(self):
        self.engine: MongoClient = MongoClient(DatabaseSettings.db_url)
        self.db = self.engine["finance"]
        self.user_collection = self.db["users"]