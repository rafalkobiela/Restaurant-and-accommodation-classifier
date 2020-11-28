import os

import pandas as pd

from config.config import Config


class DataProvider:
    def __init__(self, data=None):
        if data is None:
            config = Config()
            data_path = os.path.join(config.data_directory, config.training_data_file)
            self.data = pd.read_csv(data_path)
        else:
            self.data = pd.read_csv(data)

    def get_data(self) -> pd.DataFrame:
        return self.data
