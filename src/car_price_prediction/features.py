from __future__ import annotations

from datetime import datetime

import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()

    current_year = datetime.now().year

    if "year" in data.columns and "car_age" not in data.columns:
        data["car_age"] = current_year - pd.to_numeric(data["year"], errors="coerce")

    numeric_candidates = [
        "year",
        "mileage",
        "engine_size",
        "horsepower",
        "car_age",
    ]
    numeric_columns = [col for col in numeric_candidates if col in data.columns]

    categorical_candidates = [
        "brand",
        "model",
        "fuel_type",
        "transmission",
        "body_type",
        "color",
    ]
    categorical_columns = [col for col in categorical_candidates if col in data.columns]

    feature_columns = numeric_columns + categorical_columns
    if not feature_columns:
        raise ValueError(
            "No supported feature columns found. Add columns such as year, mileage, brand or transmission."
        )

    return data[feature_columns]
