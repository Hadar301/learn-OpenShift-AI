from loguru import logger
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_and_preprocess_data() -> pd.DataFrame:
    """
    Load data from a sickit-learn dataset and preprocess it.
    """

    # Load dataset
    logger.info("Loading and preprocessing data")
    df = sns.load_dataset("titanic")
    logger.debug(f"Dataset loaded successfully, it has the shape of {df.shape}")

    # Drop irrelevant or high-missing-value columns
    logger.info("Dropping irrelevant columns")
    df = df.drop(columns=["deck", "embark_town", "alive", "class", "who"])

    # Drop rows with null values
    logger.info("Dropping rows with null values")
    df = df.dropna()
    logger.debug(f"Dataset after dropping null values, it has the shape of {df.shape}")

    # Encode categorical variables
    logger.info("Encoding categorical variables")
    label_encoders = {}
    for col in df.select_dtypes(include="object").columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Split features and label
    X = df.drop(columns=["survived"])
    y = df["survived"]

    # Train-test split
    logger.info("Splitting the data into training and testing sets")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    logger.debug(f"Shape of X_train: {X_train.shape}, Shape of X_test: {X_test.shape}")

    # Save to disk
    logger.info("Saving preprocessed data to disk")
    X_train.to_csv("data/X_train.csv", index=False)
    X_test.to_csv("data/X_test.csv", index=False)
    y_train.to_csv("data/y_train.csv", index=False)
    y_test.to_csv("data/y_test.csv", index=False)

    logger.info("Finished loading and preprocessing of the dataset")


if __name__ == "__main__":
    load_and_preprocess_data()
