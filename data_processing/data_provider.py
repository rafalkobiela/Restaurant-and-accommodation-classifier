import os

import pandas as pd
from pandas.errors import ParserError

from config.config import Config


class DataProvider:
    def __init__(self, data=None):
        if data is None:
            config = Config()
            data_path = os.path.join(config.data_directory, config.training_data_file)
            self.data = pd.read_csv(data_path)
        else:
            self.data = pd.read_csv(data)
            self.check_data_correctness()

    def get_data(self) -> pd.DataFrame:
        return self.data

    def check_data_correctness(self):
        column_names = self.data.columns
        if column_names[0] != "WEB_TEXT" or \
                column_names[1] != "TITLE" or \
                column_names[2] != "DESCRIPTION" or \
                column_names[3] != "KEYWORDS" or \
                column_names[4] != "TARGET":
            raise ParserError("File should have 5 columns: [WEB_TEXT,TITLE,DESCRIPTION,KEYWORDS,TARGET]")

