import numpy as np

from model import Model

from app.business.weight import Weight
from app.business.price_select import PriceSelect


class Synthetic(Model):
    """Class for management of the synthetic indexes"""
    DB_NAME = 'synthetics'

    def get_p_t_1(self):
        """Getting last synthetic index or 100 in default"""
        Pt1 = 100
        obj_id = self.data_obj['_id']
        filter_synth = {'_id': obj_id - 1}
        last_synth = Synthetic.get_elements(filter_synth)
        if len(last_synth) > 0:
            Pt1 = last_synth[0].data_obj['P']
        return Pt1

    def get_nd_array_from_list(self, list_data):
        """Returning and numpy array from a list

            Keyword arguments:
            list_data -- list to convert into a numpy array
        """
        return np.array(list_data)

    def get_nd_array_from_dict(self, dict_data):
        """Returning and numpy array from a dict

            Keyword arguments:
            dict_data -- dictionary to convert into a numpy array
        """
        list_data = []
        for index in xrange(len(dict_data) - 1):
            index_name = 'index_' + str(index + 1)
            list_data.append(dict_data[index_name])
        return self.get_nd_array_from_list(list_data)

    def get_return(self):
        """Calculating returns for synthetic index"""
        obj_id = self.data_obj['_id']
        this_nd = self.get_nd_array_from_dict(self.data_obj)
        return_nd = this_nd
        filter_last_price = {'_id': obj_id - 1}
        last_prices = PriceSelect.get_elements(filter_last_price)
        if len(last_prices) > 0:
            last_nd = self.get_nd_array_from_dict(last_prices[0].data_obj)
            return_nd = this_nd / last_nd - 1
        return return_nd

    def get_weights(self):
        """Getting weights for synthetic index calculation"""
        list_weights = []
        weights = Weight.get_elements({})
        for weight in weights:
            list_weights.append(weight.data_obj['weight'])
        return self.get_nd_array_from_list(list_weights)

    def preprocess_data(self):
        """Preprocessing synthetic index data before saving it"""
        obj_id = self.data_obj['_id']
        Pt1 = self.get_p_t_1()
        return_nd = self.get_return()
        weights_nd = self.get_weights()
        Rt = return_nd.dot(weights_nd)
        Pt = Pt1 * (1 - Rt)
        self.data_obj = {'_id': obj_id, 'P': Pt}
        return True
