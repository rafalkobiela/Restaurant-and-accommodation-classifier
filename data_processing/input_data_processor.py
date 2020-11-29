import pandas as pd

from config.config import Config
from data_processing.data_provider import DataProvider
from data_processing.label_processor import get_label_encoder


class InputDataProcessor:
    def __init__(self, data=None):
        self.config = Config()

        data_provider = DataProvider(data)
        df = data_provider.get_data()
        df = self._drop_y_null_rows(df)
        self.X = df.drop(self.config.y_column_name, axis=1)
        self.y = df[self.config.y_column_name]
        self.transform_y()

    def get_data(self):
        return self.X, self.y

    def transform_y(self):
        self.y = self.y.replace(get_label_encoder())

    def _drop_y_null_rows(self, df: pd.DataFrame):
        return df[~df[self.config.y_column_name].isna()]
