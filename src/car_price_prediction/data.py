from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_dataset(path: str | Path) -> pd.DataFrame:
    file_path = Path(path)
    suffix = file_path.suffix.lower()

    if suffix == ".csv":
        return pd.read_csv(file_path)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(file_path)

    raise ValueError(f"Unsupported file format: {suffix}")
