import pandas as pd
from quantlab.backtesting.metrics import (total_return,daily_returns,max_drawdown)

def test_total_return_positive():
    portfolio_value = pd.Series([
        10000,
        10500,
        11000
    ])
    
    result = total_return(portfolio_value)
    
    assert result == 10
    
def test_total_return_negative():
    portfolio_value = pd.Series([
        10000,
        9500,
        9000
    ])
    
    result = total_return(portfolio_value)
    
    assert result == -10
    
def test_total_return_zero():
    portfolio_value = pd.Series([
        10000,
        10000
    ])
    
    result = total_return(portfolio_value)
    
    assert result == 0
    
def test_daily_returns():
    portfolio_value = pd.Series([
        100,
        110,
        121
    ])
    
    result = daily_returns(portfolio_value)
    
    expected = pd.Series([
        0.10,
        0.10
    ])
    
    pd.testing.assert_series_equal(
        result.reset_index(drop=True),
        expected,
        check_names=False
    )
    
def test_daily_returns_no_nan():
    portfolio_value = pd.Series([
        100,
        105,
        110
    ])
    
    result = daily_returns(portfolio_value)
    
    assert result.isna().sum() == 0
    
def test_max_drawdown():
    portfolio_value = pd.Series([
        10000,
        12000,
        10000
    ])
    
    result = max_drawdown(portfolio_value)
    
    assert result == -16.666666666666664
    
def test_max_drawdown_no_loss():
    portfolio_value = pd.Series([
        10000,
        11000,
        12000
    ])
    
    result = max_drawdown(portfolio_value)
    
    assert result == 0