import logging

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import max_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def split_data(data: pd.DataFrame, parameters: dict) -> tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    X = data[parameters["features"]]
    y = data["price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """Trains the linear regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor


def calculate_r2_score(y_test: pd.Series, y_pred: pd.Series) -> float:
    """Calculates the R^2 score."""
    return r2_score(y_test, y_pred)

def calculate_mae(y_test: pd.Series, y_pred: pd.Series) -> float:
    """Calculates the Mean Absolute Error."""
    return mean_absolute_error(y_test, y_pred)

def calculate_max_error(y_test: pd.Series, y_pred: pd.Series) -> float:
    """Calculates the Maximum Error."""
    return max_error(y_test, y_pred)

def evaluate_model(
    regressor: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series
) -> dict[str, float]:
    """Calculates and logs the evaluation metrics for the model.

    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.

    Returns:
        A dictionary containing R^2 score, MAE, and Max Error.
    """
    y_pred = regressor.predict(X_test)

    score = calculate_r2_score(y_test, y_pred)
    mae = calculate_mae(y_test, y_pred)
    me = calculate_max_error(y_test, y_pred)

    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient R^2 of %.3f on test data.", score)
    logger.info("Model has a Mean Absolute Error (MAE) of %.3f.", mae)
    logger.info("Model has a Maximum Error of %.3f.", me)

    return {"r2_score": score, "mae": mae, "max_error": me}