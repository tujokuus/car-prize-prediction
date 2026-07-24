# Car Price Prediction Project

This project is designed for exploratory data analysis on car sales data and for predicting vehicle prices.

## Goals

- understand the structure, quality, and distributions in the dataset
- identify the most important price-related features
- build baseline and improved machine learning models for price prediction

## Project Structure

```text
car-price-prediction/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── models/
├── notebooks/
├── reports/
├── src/
│   └── car_price_prediction/
├── tests/
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Recommended Workflow

1. Place the original CSV or Excel file in `data/raw/`.
2. Open the notebook `notebooks/01_eda_starter.ipynb`.
3. Perform an initial data quality check and EDA pass.
4. Train the first baseline model with `python -m src.car_price_prediction.train`.
5. Save processed datasets to `data/processed/` and trained models to `models/`.

## Environment Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## First Baseline Model

If your dataset includes a `price` column, you can run the baseline model with:

```bash
python -m src.car_price_prediction.train --input data/raw/cars.csv
```

By default, the script:
- reads a CSV file
- builds simple features
- splits the data into train and test sets
- trains a `RandomForestRegressor`
- prints `MAE`, `RMSE`, and `R2`

## Next Development Steps

- add more robust feature engineering
- test `XGBoost`, `LightGBM`, or `CatBoost`
- add cross-validation
- generate charts and summaries in `reports/`
