from typing import Dict

import yaml


class Config:

    def __init__(self):
        config = self._read_file()

        self.data_directory = config["model"]["data_directory"]
        self.training_data_file = config["model"]["training_data_file"]
        self.y_column_name = config["model"]["y_column_name"]
        self.transfer_model_url = config["model"]["transfer_model_url"]
        self.pipeline_save_directory = config["model"]["pipeline_save_directory"]
        self.model_directory = config["model"]["model_directory"]

    @staticmethod
    def _read_file() -> Dict:
        with open("config/config.yaml", 'r') as stream:
            config = yaml.load(stream, Loader=yaml.BaseLoader)
        return config
