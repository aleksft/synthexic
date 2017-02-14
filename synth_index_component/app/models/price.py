from model import Model
from synthetic import Synthetic


class Price(Model):
    """Class for management of the prices"""
    DB_NAME = 'prices'

    def process_other_data(self):
        """When a price is saved is necessary to process the synthetic index"""
        if self.data_obj['_id'] > 1:
            synth_obj = Synthetic(self.data_obj)
            return synth_obj.save()
        else:
            return True
