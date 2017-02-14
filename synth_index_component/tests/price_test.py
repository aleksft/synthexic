import unittest2

from test_func import TestFunctionality

from app.models.price import Price
from app.models.synthetic import Synthetic


class PriceTest(unittest2.TestCase):

    def test_save(self):
        prices_before = Price.get_elements({})
        synthetics_before = Synthetic.get_elements({})
        price_id = TestFunctionality.get_random_id()
        data_price = {'_id': price_id}
        for i in xrange(400):
            index_name = 'index_' + str(i + 1)
            data_price[index_name] = 1.98675
        new_price = Price(data_price)
        new_price.save()
        prices_after = Price.get_elements({})
        synthetics_after = Synthetic.get_elements({})
        self.assertTrue(len(prices_after) >= len(prices_before))
        self.assertTrue(len(synthetics_after) >= len(synthetics_before))
        prices_from_id = Price.get_elements({'_id': price_id})
        synthetics_from_id = Synthetic.get_elements({'_id': price_id})
        price = prices_from_id[0]
        price.data_obj['index_2'] = price.data_obj['index_1'] + 1
        price.save()
        prices_from_id_after = Price.get_elements({'_id': price_id})
        synthetics_from_id_after = Synthetic.get_elements({'_id': price_id})
        self.assertTrue(len(prices_from_id_after) > 0)
        self.assertTrue(len(synthetics_from_id_after) > 0)
        prices_after = prices_from_id_after[0]
        synthetic_after = synthetics_from_id_after[0]
        self.assertTrue('index_2' in prices_after.data_obj)
        self.assertTrue(prices_after.data_obj['index_2'] > 1.98675)


if __name__ == '__main__':
    unittest2.main()
