from quantlab.backtesting.engine import BacktestEngine
import pandas as pd


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
    
    engine =BacktestEngine(10000)
    
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
    
    engine =BacktestEngine(10000)
    
    engine.run(
        data,
        "Close",
        "Signal"
    )
    
    assert len(engine.trade_history) == 2
    assert engine.trade_history[0]["type"] == "BUY"
    assert engine.trade_history[1]["type"] == "SELL"
    
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