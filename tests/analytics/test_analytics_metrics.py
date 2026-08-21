from quantlab.analytics.metrics import (total_return, max_drawdown, volatility, sharpe_ratio, sortino_ratio, cagr)
import pytest
import pandas as pd

def test_total_return_positive():
    result = total_return(10000, 11000)
    
    assert result == 10
    
def test_total_return_negative():
    result = total_return(10000, 9000)
    
    assert result == -10
    
def test_total_return_zero():
    result = total_return(10000, 10000)
    
    assert result == 0
    
def test_total_return_invalid_initial_value():
    with pytest.raises(ValueError):
        total_return(0, 10000)
        
def test_max_drawdown_simple_loss():
    portfolio_value = pd.Series([
        10000,
        9000,
        10000,
        8000
    ])
    
    result = max_drawdown(portfolio_value)
    
    assert result == -20
    
def test_max_drawdown_no_loss():
    portfolio_value = pd.Series([
        10000,
        12000,
        15000
    ])
    
    result = max_drawdown(portfolio_value)
    
    assert result == 0
    
def test_max_drawdown_multiple_peaks():
    portfolio_value = pd.Series([
        10000,
        12000,
        9000,
        11000,
        13000,
        10000
    ])
    
    result = max_drawdown(portfolio_value)
    
    assert result == -25
    
def test_max_drawdown_empty_series():
    portfolio_value = pd.Series([])
    
    with pytest.raises(ValueError):
        max_drawdown(portfolio_value)
        
def test_max_drawdown_returns_float():
    portfolio_value = pd.Series([
            10000,
            9000,
            10000,
            8000
        ])
        
    result = max_drawdown(portfolio_value)
        
    assert isinstance(result, float)
    
def test_volatility_positive_returns():
    returns = pd.Series([
            0.01,
            -0.02,
            0.03
        ])
    
    assert volatility(returns) > 0
    
def test_volatility_constant_returns():
    returns = pd.Series([
            0.01,
            0.01,
            0.01
        ])
        
    assert volatility(returns) == 0
    
def test_volatility_high_variation():
    returns = pd.Series([
            0.10,
            -0.15,
            0.10,
            -0.15
        ])
        
    assert volatility(returns) > 10
    
def test_volatility_empty_series():
    returns = pd.Series([])
    
    with pytest.raises(ValueError):
        volatility(returns)
        
def test_volatility_returns_float():
    returns = pd.Series([
            0.10,
            -0.15,
            0.10,
            -0.15
        ])
            
    assert isinstance(volatility(returns), float)
    
def test_sharpe_ratio():
    returns = pd.Series([
        0.01,
        0.02,
        0.015,
        0.025
    ])
    
    result = sharpe_ratio(returns)
    
    assert result > 0
    
def test_sharpe_ratio_with_risk_free_rate():
    returns = pd.Series([
        0.01,
        0.02,
        0.015,
        0.025
    ])
    
    result = sharpe_ratio(
        returns,
        risk_free_rate=0.005
    )
    
    assert result > 0
    
def test_sharpe_ratio_empty_returns():
    returns = pd.Series(dtype=float)
    
    with pytest.raises(ValueError):
        sharpe_ratio(returns)
        
def test_sharpe_ratio_zero_volatility():
    returns = pd.Series([
        0.01,
        0.01,
        0.01
    ])
    
    with pytest.raises(ValueError):
        sharpe_ratio(returns)
        
def test_sortino_ratio():
    returns = pd.Series([
        0.02,
        -0.01,
        0.03,
        -0.005,
        0.015
    ])
    
    result = sortino_ratio(returns)
    
    assert result > 0
    
def test_sortino_ratio_with_risk_free_rate():
    returns = pd.Series([
        0.02,
        -0.01,
        0.03,
        -0.005,
        0.015
    ])
    
    result = sortino_ratio(
        returns,
        risk_free_rate=0.005
    )
    
    assert result > 0
    
def test_sortino_ratio_empty_returns():
    returns = pd.Series(dtype=float)
    
    with pytest.raises(ValueError):
        sortino_ratio(returns)
        
def test_sortino_ratio_without_downside_returns():
    returns = pd.Series([
        0.01,
        0.02,
        0.03
    ])
    
    with pytest.raises(ValueError):
        sortino_ratio(returns)
        
def test_sortino_ratio_zero_downside_deviation():
    returns = pd.Series([
        0.02,
        -0.01,
        0.03,
        -0.01
    ])
    
    with pytest.raises(ValueError):
        sortino_ratio(returns)
        
def test_cagr():
    result = cagr(
        initial_value=10000,
        final_values=12100,
        years=2
    )
    
    assert result == pytest.approx(0.10)
    
def test_cagr_fractional_years():
    result = cagr(
        initial_value=10000,
        final_values=11000,
        years=0.5
    )
    
    assert result == pytest.approx(0.21)
    
def test_cagr_invalid_initial_value():
    with pytest.raises(ValueError):
        cagr(
            initial_value=0,
            final_values=10000,
            years=1
        )
        
def test_cagr_negative_initial_value():
    with pytest.raises(ValueError):
        cagr(
            initial_value=-10000,
            final_values=12000,
            years=1
        )
        
def test_cagr_invalid_final_value():
    with pytest.raises(ValueError):
        cagr(
            initial_value=10000,
            final_values=0,
            years=1
        )
        
def test_cagr_negative_final_value():
    with pytest.raises(ValueError):
        cagr(
            initial_value=10000,
            final_values=-5000,
            years=1
        )
        
def test_cagr_invalid_years():
    with pytest.raises(ValueError):
        cagr(
            initial_value=10000,
            final_values=12000,
            years=0
        )
        
def test_cagr_negative_years():
    with pytest.raises(ValueError):
        cagr(
            initial_value=10000,
            final_values=12000,
            years=-1
        )
        
