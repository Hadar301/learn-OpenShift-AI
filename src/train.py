from loguru import logger
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os


def load_data():
    X_train = pd.read_csv("data/X_train.csv")
    y_train = pd.read_csv("data/y_train.csv").values.ravel()
    logger.debug(
        f"finished loading data, data set has the shape of {X_train.shape} with labels of shape {y_train.shape}"
    )
    assert (
        X_train.shape[0] == y_train.shape[0]
    ), "X_train and y_train must have the same number of rows"
    return X_train, y_train


def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    logger.debug("model trained successfull")
    return model


def save_model(model):
    model_dir = "model"
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")
    logger.debug(f"saving model to {model_path}")
    joblib.dump(model, model_path)


if __name__ == "__main__":
    logger.info("Loading training data")
    X_train, y_train = load_data()
    logger.info("Training model")
    model = train_model(X_train, y_train)
    logger.info("Saving model")
    save_model(model)
