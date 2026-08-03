from quantlab.strategies.moving_average import MovingAverageStrategy
import pytest
import pandas as pd
from quantlab.strategies.base import Strategy

def test_moving_average_creation():
    strategy = MovingAverageStrategy(5, 20)
    
    assert strategy.short_window == 5
    assert strategy.long_window == 20
    
def test_short_window_invalid():
    with pytest.raises(ValueError):
        MovingAverageStrategy(0, 20)    

def test_long_window_invalid():
    with pytest.raises(ValueError):
        MovingAverageStrategy(5, 0)
        
def test_prepare_data_adds_sma():
    data = pd.DataFrame({
        "Close": [10, 20, 30, 40, 50]
    })
    
    strategy = MovingAverageStrategy(2, 3)
    
    result = strategy.prepare_data(data)
    
    assert "SMA_short" in result.columns
    assert "SMA_long" in result.columns
    
def test_generate_buy_signal():
    strategy = MovingAverageStrategy(2, 5)
    
    row = pd.Series({
        "SMA_short": 20,
        "SMA_long": 10
    })
    
    assert strategy.generate_signal(row) == 1
    
def test_generate_sell_signal():
    strategy = MovingAverageStrategy(2, 5)
    
    row = pd.Series({
        "SMA_short": 10,
        "SMA_long": 20
    })
    
    assert strategy.generate_signal(row) == -1
    
def test_generate_hold_signal():
    strategy = MovingAverageStrategy(2, 5)
    
    row = pd.Series({
        "SMA_short": 10,
        "SMA_long": 10
    })
    
    assert strategy.generate_signal(row) == 0
    
def test_short_window_greater_than_long_window():
    with pytest.raises(ValueError):
        MovingAverageStrategy(20, 5)
        
def test_generate_hold_with_nan_values():
    strategy = MovingAverageStrategy(5, 20)
    
    row = pd.Series({
        "SMA_short": float("nan"),
        "SMA_long": 10
    })
    
    assert strategy.generate_signal(row) == 0
    
def test_prepare_data_does_not_modify_original_data():
    data = pd.DataFrame({
        "Close": [10, 20, 30, 40, 50]
    })
    
    strategy = MovingAverageStrategy(2, 3)
    
    strategy.prepare_data(data)
    
    assert "SMA_short" not in data.columns
    
def test_prepare_data_invalid_column():
    data = pd.DataFrame({
        "Price": [10, 20, 30]
    })
    
    strategy = MovingAverageStrategy(2, 3)
    
    with pytest.raises(KeyError):
        strategy.prepare_data(data, "Close")
        
def test_moving_average_is_strategy():
    strategy = MovingAverageStrategy(2, 5)
    
    assert isinstance(strategy, Strategy)