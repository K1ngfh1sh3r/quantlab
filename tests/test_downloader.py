from datetime import date
from quantlab.data.downloader import download_market_data
import pandas as pd


def test_download_market_data_returns_dataframe():
    data = download_market_data("AAPL", date(2024, 1, 1), date(2025, 1, 1))
    assert isinstance(data, pd.DataFrame)


def test_download_market_data_not_empty():
    data = download_market_data("AAPL", date(2024, 1, 1), date(2025, 1, 1))
    assert not data.empty


def test_download_market_data_columns():
    data = download_market_data("AAPL", date(2024, 1, 1), date(2025, 1, 1))
    expected_columns = ["Open", "High", "Low", "Close", "Volume"]
    assert set(data.columns) == set(expected_columns)
