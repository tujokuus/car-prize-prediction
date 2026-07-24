# Car Price Prediction Project

Tama projekti on rakennettu autojen myyntidatan exploratory data analysis -tyohon ja hintojen ennustamiseen.

## Tavoite

- ymmartaa datan rakennetta, laatua ja jakaumia
- tunnistaa hinnan kannalta merkittavat muuttujat
- rakentaa baseline- ja jatkomallit auton hinnan ennustamiseen

## Projektirakenne

```text
car prediction ml project/
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

## Suositeltu eteneminen

1. Tuo alkuperainen CSV tai Excel-tiedosto kansioon `data/raw/`.
2. Avaa notebook `notebooks/01_eda_starter.ipynb`.
3. Tee datan laadun tarkistus ja ensimmainen EDA.
4. Rakenna ensimmainen baseline-malli komennolla `python -m src.car_price_prediction.train`.
5. Tallenna prosessoitu data kansioon `data/processed/` ja mallit kansioon `models/`.

## Ensiasennus

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Ensimmainen baseline

Kun datasetissa on sarake `price`, voit kokeilla baselinea:

```bash
python -m src.car_price_prediction.train --input data/raw/cars.csv
```

Oletuksena skripti:
- lukee CSV:n
- rakentaa yksinkertaiset piirteet
- jakaa datan train/test-osaan
- kouluttaa `RandomForestRegressor`-mallin
- tulostaa `MAE`, `RMSE` ja `R2`

## Seuraavat kehitysaskeleet

- lisata tarkempi feature engineering
- testata `XGBoost`, `LightGBM` tai `CatBoost`
- lisata cross-validation
- tuottaa kuvat ja yhteenvedot kansioon `reports/`
