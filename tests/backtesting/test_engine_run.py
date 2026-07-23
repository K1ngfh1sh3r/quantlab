from quantlab.backtesting.engine import BacktestEngine
import pandas as pd
import pytest


def test_run_returns_dataframe():
    data = pd.DataFrame({
        "Close": [100, 110, 120],
        "Signal": [0, 1, 0]
    })

    engine = BacktestEngine(10000)

    result = engine.run(
        data,
        "Close",
        "Signal"
    )

    assert isinstance(result, pd.DataFrame)
    
def test_run_contains_portfolio_value():
    data = pd.DataFrame({
        "Close": [100, 110, 120],
        "Signal": [0, 1, 0]
    })
    
    engine = BacktestEngine(10000)
    
    result = engine.run(
        data,
        "Close",
        "Signal"
    )
    
    assert "Portfolio_Value" in result.columns
    
def test_run_shares():
    data = pd.DataFrame({
        "Close": [100, 110, 120],
        "Signal": [0, 1, 0]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        "Close",
        "Signal"
    )
    
    assert engine.portfolio.shares == 1
    
def test_run_trade_history():
    data = pd.DataFrame({
        "Close": [100, 110, 120],
        "Signal": [0, 1, 0]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        "Close",
        "Signal"
    )
    
    assert len(engine.portfolio.trade_history) == 1
    
def test_run_sell_signal():
    data = pd.DataFrame({
        "Close": [100, 110, 120],
        "Signal": [1, 0, -1]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        "Close",
        "Signal"
    )
    
    assert engine.portfolio.shares == 0
    
def test_run_buy_and_sell_history():
    data = pd.DataFrame({
        "Close": [100, 110, 120],
        "Signal": [1, 0, -1]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        "Close",
        "Signal"
    )
    
    assert len(engine.portfolio.trade_history) == 2
    assert engine.portfolio.trade_history[0].trade_type == "BUY"
    assert engine.portfolio.trade_history[1].trade_type == "SELL"
    
def test_run_portfolio_value_calculation():
    data = pd.DataFrame({
        "Close": [100, 120],
        "Signal": [1, -1]
    })
    
    engine = BacktestEngine(10000)
    
    result = engine.run(
        data,
        "Close",
        "Signal"
    )
    
    assert result["Portfolio_Value"].iloc[-1] == 10020
    
def test_run_invalid_price_column():
    data = pd.DataFrame({
        "Close": [100, 110],
        "Signal": [0, 1]
    })
    
    engine = BacktestEngine(10000)
    
    with pytest.raises(KeyError):
        engine.run(
            data,
            "Price",
            "Signal"
        )

def test_run_invalid_signal_column():
    data = pd.DataFrame({
        "Close": [100, 110],
        "Signal": [0, 1]
    })
    
    engine = BacktestEngine(10000)
    
    with pytest.raises(KeyError):
        engine.run(
            data,
            "Close",
            "Action"
        )
        
def test_run_invalid_signal_value():
    data = pd.DataFrame({
        "Close":[100],
        "Signal":[5]
    })
    
    engine = BacktestEngine(10000)
    
    with pytest.raises(ValueError):
        engine.run(
            data,
            "Close",
            "Signal"
        )
        
def test_run_portfolio_evolution():
    data = pd.DataFrame({
        "Close": [100, 120, 130],
        "Signal": [1, 0, 0]
    })

    engine = BacktestEngine(10000)
    
    result = engine.run(
        data,
        "Close",
        "Signal"
    )
    
    assert result["Portfolio_Value"].iloc[0] == 10000
    assert result["Portfolio_Value"].iloc[1] == 10020
    assert result["Portfolio_Value"].iloc[2] == 10030
