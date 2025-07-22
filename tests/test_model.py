import os

from src.model import train_model


def test_train_model():
    train_model()
    assert os.path.exists("model.pkl"), "Model file not created"
