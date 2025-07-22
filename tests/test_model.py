import os

from src.model import train_model


def test_train_model():
    train_model()
    assert os.path.exists("models/random_forest_model.joblib"), "Model file not created"
