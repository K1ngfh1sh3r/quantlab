import pandas as pd
from quantlab.indicators.moving_average import (simple_moving_average,exponential_moving_average)
import pytest

data = pd.DataFrame({
    "Close": [10, 11, 12, 13, 14, 15]
})

def test_simple_moving_average_returns_series():
    sma = simple_moving_average(data, "Close", 3)
    assert isinstance(sma, pd.Series)
    
@pytest.mark.parametrize(
    "window",
    [
    0, 
    -1, 
    -10
    ]
)    
def test_simple_moving_average_invalid_window(window):
    with pytest.raises(ValueError):
        simple_moving_average(data, "Close", window)
        
def test_simple_moving_average_invalid_column():
    with pytest.raises(KeyError):
        simple_moving_average(data, "Price", 3)
        
def test_simple_moving_average_calculation():
    expected = pd.Series([None, None, 11, 12, 13, 14],name="Close")
    result = simple_moving_average(data, "Close", 3)
    pd.testing.assert_series_equal(result, expected)
    
def test_simple_moving_average_preserves_index():
    sma = simple_moving_average(data, "Close", 3)
    assert sma.index.equals(data.index)
    
def test_simple_moving_average_with_different_column():
    data = pd.DataFrame({
    "Open": [1,2,3,4],
    "Close": [10,11,12,13]
    })
    sma = simple_moving_average(data, "Open", 2)
    expected = pd.Series([None, 1.5, 2.5, 3.5], name="Open")
    pd.testing.assert_series_equal(sma,expected)
  
def test_exponential_moving_average_returns_series():
    ema = exponential_moving_average(data, "Close", 3)
    assert isinstance(ema, pd.Series)
    
@pytest.mark.parametrize(
    "window",
    [
    0, 
    -1, 
    -10
    ]
)    
def test_exponential_moving_average_invalid_window(window):
    with pytest.raises(ValueError):
        exponential_moving_average(data, "Close", window)
        
def test_exponential_moving_average_invalid_column():
    with pytest.raises(KeyError):
        exponential_moving_average(data, "Price", 3)
        
def test_exponential_moving_average_calculation():
    expected = data["Close"].ewm(span=3,adjust=False).mean()
    result = exponential_moving_average(data, "Close", 3)
    pd.testing.assert_series_equal(result, expected)
    
def test_exponential_moving_average_preserves_index():
    ema = exponential_moving_average(data, "Close", 3)
    assert ema.index.equals(data.index)
    
def test_exponential_moving_average_with_different_column():
    data = pd.DataFrame({
    "Open": [1,2,3,4],
    "Close": [10,11,12,13]
    })
    ema = exponential_moving_average(data, "Open", 2)
    expected = data["Open"].ewm(span=2,adjust=False).mean()
    pd.testing.assert_series_equal(ema,expected)