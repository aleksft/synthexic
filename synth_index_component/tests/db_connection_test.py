import unittest2

from app.db.db_connection import DBConnection


class DBConnectionTest(unittest2.TestCase):
    DATASET_NAME = 'testDB'

    def test_save(self):
        connection = DBConnection(self.DATASET_NAME)
        collection_before = connection.get_elements({})
        obj_id = len(collection_before) + 1
        connection.save({'_id': obj_id, 'index_1': 1.2345})
        collection_after = connection.get_elements({})
        self.assertEqual(len(collection_after), len(collection_before) + 1)
        collection_index_1 = connection.get_elements({'index_1': 1.2345})
        self.assertTrue(len(collection_index_1) > 0)
        dict_obj = collection_index_1[0]
        new_index_1 = dict_obj['index_1'] + 0.89
        dict_obj['index_1'] = new_index_1
        collection_before_1 = connection.get_elements({'index_1': new_index_1})
        connection.save(dict_obj)
        collection_after_1 = connection.get_elements({'index_1': new_index_1})
        self.assertEqual(len(collection_after_1), len(collection_before_1) + 1)


if __name__ == '__main__':
    unittest2.main()
