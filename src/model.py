import os

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from src.dataset import download_and_save_iris

MODEL_PATH = "models/random_forest_model.joblib"


def train_model():
    df, _ = download_and_save_iris()
    x = df.drop(columns=["species"])
    y = df["species"]

    x_train, _, y_train, _ = train_test_split(x, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)


if __name__ == "__main__":
    train_model()
    print(f"Model trained and saved to {MODEL_PATH}")
