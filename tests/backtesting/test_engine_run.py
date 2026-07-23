from quantlab.backtesting.engine import BacktestEngine
from quantlab.backtesting.trade import Trade
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
    
    assert engine.shares == 1
    
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
    
    assert len(engine.trade_history) == 1
    
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
    
    assert engine.shares == 0
    
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
    
    assert len(engine.trade_history) == 2
    assert engine.trade_history[0].trade_type == "BUY"
    assert engine.trade_history[1].trade_type == "SELL"
    
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
    
def test_trade_creation():
    trade = Trade(
        "BUY",
        100,
        5
    )

    assert trade.trade_type == "BUY"
    assert trade.price == 100
    assert trade.quantity == 5
    
def test_trade_type():
    engine = BacktestEngine(10000)
    
    engine.buy(100, 5)
    
    assert isinstance(engine.trade_history[0], Trade)
    
def test_trade_return():
    engine = BacktestEngine(10000)
    
    engine.buy(100, 5)
    
    trade = engine.trade_history[0]
    
    assert trade.trade_type == "BUY"
    assert trade.price == 100
    assert trade.quantity == 5
    
def test_trade_value():
    trade = Trade(
        "BUY",
        100,
        5
    )
    
    assert trade.value == 500
    
def test_trade_sell():
    trade = Trade(
        "SELL",
        120,
        10
    )
    
    assert trade.trade_type == "SELL"
    assert trade.value == 1200