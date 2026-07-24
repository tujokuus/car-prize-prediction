from __future__ import annotations

import argparse
from math import sqrt

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from .data import load_dataset
from .features import build_features


def train_baseline(df: pd.DataFrame, target_column: str = "price") -> dict[str, float]:
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataset.")

    X = build_features(df)
    y = pd.to_numeric(df[target_column], errors="coerce")

    valid_rows = y.notna()
    X = X.loc[valid_rows]
    y = y.loc[valid_rows]

    numeric_columns = X.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns = [col for col in X.columns if col not in numeric_columns]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                    ]
                ),
                numeric_columns,
            ),
            (
                "cat",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("encoder", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical_columns,
            ),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", RandomForestRegressor(n_estimators=200, random_state=42)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    return {
        "mae": mean_absolute_error(y_test, predictions),
        "rmse": sqrt(mse),
        "r2": r2_score(y_test, predictions),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Train a baseline car price model.")
    parser.add_argument("--input", required=True, help="Path to CSV or Excel dataset.")
    parser.add_argument(
        "--target",
        default="price",
        help="Target column name. Default: price",
    )
    args = parser.parse_args()

    df = load_dataset(args.input)
    metrics = train_baseline(df=df, target_column=args.target)

    print("Baseline metrics")
    print(f"MAE:  {metrics['mae']:.2f}")
    print(f"RMSE: {metrics['rmse']:.2f}")
    print(f"R2:   {metrics['r2']:.4f}")


if __name__ == "__main__":
    main()
