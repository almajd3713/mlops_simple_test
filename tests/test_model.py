from src.model import train_model
import os

def test_train_model():
  train_model()
  assert os.path.exists("model.pkl"), "Model file not created"