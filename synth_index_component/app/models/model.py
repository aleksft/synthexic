from app.db.db_connection import DBConnection


class Model():
    """Generic class for persitent objects in the system"""
    DB_NAME = ''
    data_obj = {}

    def __init__(self, dict_obj):
        """Initizalizes a model object based on a dictionary, if the day key
            appears in the dictionary it will be changed by the '_id' key

            Keyword arguments:
            dict_obj -- dictionary with the object's data
        """
        if 'day' in dict_obj:
            dict_obj['_id'] = dict_obj['day']
            del dict_obj["day"]
        self.data_obj = dict_obj

    def preprocess_data(self):
        """Calculation of necessary data before save the objetct"""
        return True

    def process_other_data(self):
        """Processing of related data with the current object"""
        return True

    def save(self):
        """Preprocessing, saving and postprocessing of the current object, if
            returns false, an error occurred
        """
        if self.preprocess_data():
            connection = DBConnection(self.DB_NAME)
            result_save = connection.save(self.data_obj)
            result_process = self.process_other_data()
            return (result_save and result_process)
        else:
            return False

    @classmethod
    def get_elements(kls, filters):
        """Filtering of class objects"""
        elements = []
        collection = DBConnection(kls.DB_NAME).get_elements(filters)
        for item in collection:
            elements.append(kls(item))
        return elements
