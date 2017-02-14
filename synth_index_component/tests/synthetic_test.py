import unittest2

from test_func import TestFunctionality

from app.models.synthetic import Synthetic


class SyntheticTest(unittest2.TestCase):

    def test_save(self):
        synthetics_before = Synthetic.get_elements({})
        synth_id = TestFunctionality.get_random_id()
        data_synth = {'_id': synth_id}
        for i in xrange(400):
            index_name = 'index_' + str(i + 1)
            data_synth[index_name] = 0.899999
        print data_synth
        new_synthetic = Synthetic(data_synth)
        new_synthetic.save()
        synthetics_after = Synthetic.get_elements({})
        self.assertTrue(len(synthetics_after) >= len(synthetics_before))


if __name__ == '__main__':
    unittest2.main()
