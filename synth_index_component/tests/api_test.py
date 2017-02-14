import os
import tempfile
import unittest2

from flask import json

from test_func import TestFunctionality

from manage import app
from app.settings import TestConfig
from app.models.price import Price


class ApiTestCase(unittest2.TestCase):

    def setUp(self):
        app.config.from_object(TestConfig)
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_prices(self):
        headers = {'Content-Type': 'application/json'}
        price_id = TestFunctionality.get_random_id()
        data = {'day': price_id}
        for i in xrange(400):
            index_name = 'index_' + str(i + 1)
            data[index_name] = 400 / (i + 1)
        response = self.app.post('/api/v1/prices', data=json.dumps(data),
                                 headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.data)['response'])


if __name__ == '__main__':
    unittest2.main()
