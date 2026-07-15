import pandas as pd
import pytest
from quantlab.indicators.momentum import relative_strength_index

data = pd.DataFrame({
    "Close": [
        10, 11, 10, 12,
        13, 12, 14,
        15, 14, 16
    ]
})

def test_relative_strength_index_returns_series():
    rsi = relative_strength_index(data,"Close",3)
    assert isinstance(rsi, pd.Series)
    
@pytest.mark.parametrize(
    "window",
    [
    0, 
    -1, 
    -10
    ]
)   
    
def test_relative_strength_index_invalid_window(window):
    with pytest.raises(ValueError):
        relative_strength_index(data, "Close", window)
        
def test_relative_strength_index_invalid_column():
    with pytest.raises(KeyError):
        relative_strength_index(data, "Price", 3)
        
def test_relative_strength_index_preserves_index():
    rsi = relative_strength_index(data, "Close", 3)
    assert rsi.index.equals(data.index)
    
def test_relative_strength_index_range():
    rsi = relative_strength_index(data, "Close", 3)
    rsi  =rsi.dropna()
    assert ((rsi >= 0) & (rsi <= 100)).all()
    
def test_relative_strength_index_calculation():
    prices = data["Close"]
    delta = prices.diff()
    
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    
    avg_gain = gain.ewm(
        alpha=1/3,
        adjust=False
    ).mean()
    
    avg_loss = loss.ewm(
        alpha=1/3,
        adjust=False
    ).mean()
    
    rs = avg_gain / avg_loss.replace(0, float("nan"))
    
    expected = 100 - (100/ (1 + rs))
    
    result = relative_strength_index(
        data,
        "Close",
        3
    )
    
    pd.testing.assert_series_equal(result,expected,check_names=False)