import pandas as pd  
import pytest
from quantlab.strategies.moving_average_cross import moving_average_crossover

data = pd.DataFrame({
    "Close": [
        10, 11, 10, 12,
        13, 12, 14,
        15, 14, 16
    ]
})

def test_moving_average_cross_returns_dataframe():
    result = moving_average_crossover(data, "Close", 3, 5)
    assert isinstance(result, pd.DataFrame)
    
def test_strategy_contains_signal_column():
    result = moving_average_crossover(data, "Close", 3, 5)
    assert "Signal" in result.columns
    
def test_invalid_window():
    with pytest.raises(ValueError):
        moving_average_crossover(data, "Close", 5, 3)
        
def test_signal_values_are_valid():
    result = moving_average_crossover(data, "Close", 3, 5)
    assert set(result["Signal"].unique()).issubset({-1,0,1})
    
@pytest.mark.parametrize(
    "short_window,long_window",
    [
        (0, 5),
        (-1, 5),
        (3, 0),
        (3, -5)
    ]
)
def test_invalid_window_values(short_window, long_window):
    with pytest.raises(ValueError):
        moving_average_crossover(data, "Close", short_window, long_window)
        
def test_strategy_contains_moving_average_columns():
    result = moving_average_crossover(data, "Close", 3, 5)
    
    assert "Short_MA" in result.columns
    assert "Long_MA" in result.columns
    
def test_invalid_column():
    with pytest.raises(KeyError):
        moving_average_crossover(data, "Price", 3, 5)
        
def test_no_signal_before_enough_data():
    result = moving_average_crossover(data, "Close", 3, 5)
    assert result["Signal"].iloc[:4].eq(0).all()
    
def test_strategy_preserves_original_data():
    result = moving_average_crossover(data, "Close", 3, 5)
    pd.testing.assert_series_equal(result["Close"], data["Close"])
    
def test_signal_logic():
    result = moving_average_crossover(data, "Close", 3, 5)
    
    assert (
        result.loc[
            result["Short_MA"] > result["Long_MA"],
            "Signal"
        ] == 1
    ).all()
    
    assert (
        result.loc[
            result["Short_MA"] < result["Long_MA"],
            "Signal"
        ] == -1
    ).all()