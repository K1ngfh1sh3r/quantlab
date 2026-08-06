from quantlab.analytics.utils import calculate_returns
import pandas as pd
import pytest

def test_calculate_returns_simple():
    portfolio_value = pd.Series([
        100,
        110,
        120
    ])
    
    result = calculate_returns(portfolio_value)
    
    assert pd.isna(result.iloc[0])
    assert result.iloc[1] == pytest.approx(0.10)
    assert result.iloc[2] == pytest.approx(0.0909, rel=1e-3)
    
def test_calculate_returns_negative():
    portfolio_value = pd.Series([
        100,
        90,
        81
    ])
    
    result = calculate_returns(portfolio_value)
    
    assert pd.isna(result.iloc[0])
    assert result.iloc[1] == pytest.approx(-0.10)
    assert result.iloc[2] == pytest.approx(-0.10)
    
def test_calculate_returns_empty_series():
    portfolio_value = pd.Series([])

    with pytest.raises(ValueError):
        calculate_returns(portfolio_value)
        
def test_calculate_returns_returns_series():
    portfolio_value = pd.Series([
        100,
        110,
        120
    ])

    result = calculate_returns(portfolio_value)

    assert isinstance(result, pd.Series)
    
def test_calculate_returns_first_value_nan():
    portfolio_value = pd.Series([
        100,
        110,
        120
    ])

    result = calculate_returns(portfolio_value)

    assert pd.isna(result.iloc[0])