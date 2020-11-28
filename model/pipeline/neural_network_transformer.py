import tensorflow as tf
import tensorflow_hub as hub
from sklearn.base import TransformerMixin, BaseEstimator

from config.config import Config


class NeuralNetworkTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.config = Config()
        self._create_neural_network()
        self.model.compile(optimizer='adam',
                           loss=tf.losses.BinaryCrossentropy(from_logits=False),
                           metrics=["accuracy"])

    def fit(self, X, y):
        self.model.fit(X,
                       y,
                       epochs=50,
                       batch_size=128,
                       verbose=1)
        return self

    def transform(self, X):
        predictions = self.model.predict(X)
        predictions[X == ""] = 0.5
        return predictions

    def _create_neural_network(self):
        tf.random.set_seed(1234)
        hub_layer = hub.KerasLayer(self.config.transfer_model_url, output_shape=[32], input_shape=[],
                                   dtype=tf.string, trainable=False)
        self.model = tf.keras.Sequential()
        self.model.add(hub_layer)
        self.model.add(tf.keras.layers.Dense(16, activation='relu'))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
