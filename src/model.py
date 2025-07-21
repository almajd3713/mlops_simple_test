from dataset import download_and_save_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import os

import joblib
model_path = "models/random_forest_model.joblib"

def train_model():
  df, _ = download_and_save_iris()
  X = df.drop(columns=['species'])
  y = df['species']
  
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  
  model = RandomForestClassifier(n_estimators=100, random_state=42)
  model.fit(X_train, y_train)
  
  os.makedirs("models", exist_ok=True)
  joblib.dump(model, model_path)

if __name__ == "__main__":
  train_model()
  print(f"Model trained and saved to {model_path}")