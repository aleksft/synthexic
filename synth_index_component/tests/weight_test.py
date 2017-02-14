import unittest2

from app.business.weight import Weight


class WeightTest(unittest2.TestCase):

    def test_get_elements(self):
        weights = Weight.get_elements({})
        self.assertTrue(len(weights) > 0)
        weight_1 = Weight.get_elements({'_id': 1})
        self.assertEqual(len(weight_1), 1)


if __name__ == '__main__':
    unittest2.main()
