import numpy as np
from sklearn.metrics import precision_score, recall_score, accuracy_score

from config.config import Config
from data_processing.input_data_processor import InputDataProcessor
from data_processing.label_processor import get_label_decoder
from dtos.scoring_response import ScoringResult
from model.pipeline.pipeline import create_pipeline
from model.pipeline.pipeline_serializer import save_pipeline, load_pipeline


class Model:
    def __init__(self):
        self.model = create_pipeline()
        self.config = Config()

    def train(self):
        input_data_processor = InputDataProcessor()
        X, y = input_data_processor.get_data()
        self.model.fit(X, y)

    def predict(self, web_text: str, title: str, description: str, keywords: str):
        new_observation = np.array([web_text, title, description, keywords], dtype="object").reshape(1, -1)
        label_decoder = get_label_decoder()
        pred = self.model.predict(new_observation)[0]
        return label_decoder[pred]

    def score(self, data) -> ScoringResult:

        data_processor = InputDataProcessor(data)
        X, y = data_processor.get_data()

        predictions = self.model.predict(X)

        precision = precision_score(y, predictions, pos_label=0)
        recall = recall_score(y, predictions, pos_label=0)
        accuracy = accuracy_score(y, predictions)

        return ScoringResult(precision, recall, accuracy)

    def save_model(self):
        save_pipeline(self.model)

    def load_model(self):
        self.model = load_pipeline()
