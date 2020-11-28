from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
import numpy as np

from model.pipeline.neural_network_transformer import NeuralNetworkTransformer


def create_pipeline():
    column_transformer = _create_column_transformer()

    return Pipeline([
        ("null_imputer", SimpleImputer(missing_values=np.nan, strategy='constant', fill_value="")),
        ("neural_network", column_transformer),
        ("classifier", XGBClassifier())
    ])


def _create_column_transformer() -> ColumnTransformer:
    return ColumnTransformer(transformers=[
        ("web_text", NeuralNetworkTransformer(), [0]),
        ("title", NeuralNetworkTransformer(), [1]),
        ("description", NeuralNetworkTransformer(), [2]),
        ("keywords", NeuralNetworkTransformer(), [3])
    ])
