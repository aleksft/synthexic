from app.db.db_connection import DBConnection


class Business():
    """Generic class for calculated objects in the system"""
    DB_NAME = ''
    data_obj = {}

    def __init__(self, dict_obj):
        """Initizalizes a model object based on a dictionary

            Keyword arguments:
            dict_obj -- dictionary with the object's data
        """
        self.data_obj = dict_obj

    @classmethod
    def get_elements(kls, filters):
        """Filtering of class objects"""
        elements = []
        collection = DBConnection(kls.DB_NAME).get_elements(filters)
        for item in collection:
            elements.append(kls(item))
        return elements
