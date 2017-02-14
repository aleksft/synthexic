import unittest2

from app.business.price_select import PriceSelect


class PriceSelectTest(unittest2.TestCase):

    def test_get_elements(self):
        prices_select = PriceSelect.get_elements({})
        self.assertTrue(len(prices_select) > 0)
        prices_id = prices_select[0].data_obj['_id']
        price_select_1 = PriceSelect.get_elements({'_id': prices_id})
        self.assertEqual(len(price_select_1), 1)


if __name__ == '__main__':
    unittest2.main()
