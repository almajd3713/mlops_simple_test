from src.dataset import load_dataset
import os

def test_load_dataset():
  load_dataset()
  assert os.path.exists("data.csv"), "Dataset file not created"