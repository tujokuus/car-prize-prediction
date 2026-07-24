from pathlib import Path

from src.car_price_prediction.data import load_dataset


def test_project_structure_exists() -> None:
    assert Path("src/car_price_prediction").exists()


def test_load_dataset_rejects_unknown_extension(tmp_path) -> None:
    dummy_file = tmp_path / "cars.txt"
    dummy_file.write_text("placeholder", encoding="utf-8")

    try:
        load_dataset(dummy_file)
    except ValueError as exc:
        assert "Unsupported file format" in str(exc)
    else:
        raise AssertionError("Expected ValueError for unsupported file format")
