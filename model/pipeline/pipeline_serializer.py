import os
import pickle
import tensorflow as tf
import tensorflow_hub as hub
from sklearn.pipeline import Pipeline

from config.config import Config


def save_pipeline(pipeline: Pipeline):
    config = Config()

    for i in range(4):
        model = pipeline.steps[1][1].transformers_[i][1].model
        model_path = os.path.join(config.model_directory, f"tf_{i}.h5")
        model.save(model_path)

    for i in range(4):
        pipeline.steps[1][1].transformers[i][1].model = None
        pipeline.steps[1][1].transformers_[i][1].model = None

    pipeline_path = os.path.join(config.model_directory, "p1.pkl")
    with open(pipeline_path, "wb") as f:
        pickle.dump(pipeline, f)


def load_pipeline() -> Pipeline:
    config = Config()
    pipeline_path = os.path.join(config.model_directory, "p1.pkl")
    with open(pipeline_path, "rb") as f:
        pipeline = pickle.load(f)

    for i in range(4):
        model_path = os.path.join(config.model_directory, f"tf_{i}.h5")
        model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer': hub.KerasLayer})
        pipeline.steps[1][1].transformers_[i][1].model = model

    return pipeline
