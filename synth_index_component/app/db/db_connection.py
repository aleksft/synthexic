import pymongo

from flask import current_app as app
from pymongo import MongoClient

from app.settings import Config


class DBConnection():
    """Class to connect to the database"""

    def __init__(self, name_dataset):
        """Initizalizes the connection in an specific dataset

            Keyword arguments:
            name_dataset -- name of the dataset to connect to
        """
        self.client = MongoClient(self.__class__.get_db_connection())
        self.db = self.client[self.__class__.get_database()]
        self.dataset = self.db[name_dataset]

    def save(self, dict_obj):
        """Saving a document in the dataset"""
        id_obj = dict_obj['_id']
        result = self.dataset.update_one({'_id': id_obj}, {'$set': dict_obj},
                                         upsert=True)
        return (result.upserted_id == id_obj)

    def get_elements(self, filters):
        """Filtering elements from the dataset"""
        elements = []
        cursor = self.dataset.find(filters).sort([('_id', pymongo.ASCENDING)])
        for element in cursor:
            elements.append(element)
        return elements

    @staticmethod
    def get_db_connection():
        """Getting DB Connection from app or Config in default"""
        return app.config['DB_CONNECTION'] if app else Config.DB_CONNECTION

    @staticmethod
    def get_database():
        """Getting Database from app or Config in default"""
        return app.config['DATABASE'] if app else Config.DATABASE
