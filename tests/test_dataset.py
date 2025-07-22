import os

from src.dataset import download_and_save_iris


def test_load_dataset():
    download_and_save_iris()
    assert os.path.exists("data/data.csv"), "Dataset file not created"
