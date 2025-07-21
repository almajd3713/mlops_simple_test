import os
import pandas as pd
from sklearn.datasets import load_iris

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "iris.csv")

def download_and_save_iris():
  if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
  if not os.path.isfile(DATA_FILE):
    iris = load_iris(as_frame=True)
    df = iris.frame
    df.to_csv(DATA_FILE, index=False)
    print(f"Iris dataset saved to {DATA_FILE}")
  else:
    print(f"Iris dataset already exists at {DATA_FILE}")