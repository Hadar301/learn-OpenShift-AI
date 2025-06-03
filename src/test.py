from loguru import logger
import pandas as pd
import joblib
import os

from sklearn.metrics import accuracy_score

def load_model(model_path="model/model.joblib"):
    return joblib.load(model_path)

def load_test_data():
    X_test = pd.read_csv("data/X_test.csv")
    y_test = pd.read_csv("data/y_test.csv").values.ravel()
    return X_test, y_test

def run_inference(model, X_test):
    return model.predict(X_test), model.predict_proba(X_test)

def save_predictions(predictions, probabilities, output_path="data/predictions.csv"):
    logger.debug("Saving predictions to data/predictions.csv")
    pd.DataFrame(list(zip(predictions, probabilities[:,-1])), columns=[["prediction", "probabilties"]]).to_csv(output_path, index=False)
    logger.debug(f"Predictions saved to {output_path}")

if __name__ == "__main__":
    logger.info("🚀 Running inference...")
    model = load_model()
    logger.info("✅ Model loaded")
    X_test, y_test = load_test_data()
    logger.info("✅ Test data loaded")
    preds, probabilities = run_inference(model, X_test)
    logger.info("✅ Inference done")
    save_predictions(preds, probabilities)
    logger.info("✅ Predictions saved")

    # Optional quick metric
    acc = accuracy_score(y_test, preds)
    logger.info(f"🔬 Accuracy: {acc:.4f}")