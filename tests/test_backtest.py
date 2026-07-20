from quantlab.backtesting.engine import BacktestEngine
import pytest

def test_backtest_initial_capital():
    engine = BacktestEngine(10000)
    
    assert engine.initial_capital == 10000
    assert engine.cash == 10000
    assert engine.shares == 0
    assert engine.trade_history == []
    
def test_buy():
    engine = BacktestEngine(10000)
    
    engine.buy(100, 10)
    
    assert engine.cash == 9000
    assert engine.shares == 10
    
def test_sell():
    engine = BacktestEngine(10000)
    
    engine.buy(100, 10)
    engine.sell(120, 5)
    
    assert engine.cash == 9600
    assert engine.shares == 5
    
def test_buy_creates_trade_history():
    engine = BacktestEngine(10000)
    
    engine.buy(100, 10)
    
    assert len(engine.trade_history) == 1
    assert engine.trade_history[0]["type"] == "BUY"
    
def test_buy_without_enough_cash():
    engine = BacktestEngine(1000)
    
    with pytest.raises(ValueError):
        engine.buy(500, 10)
        
def test_sell_without_enough_shares():
    engine = BacktestEngine(10000)
    
    with pytest.raises(ValueError):
        engine.sell(100, 5)
        
def test_sell_creates_trade_history():
    engine = BacktestEngine(10000)
    
    engine.buy(100, 5)
    engine.sell(120, 5)
    
    assert len(engine.trade_history) == 2
    assert engine.trade_history[1]["type"] == "SELL"
    
def test_portfolio_value_no_action():
    engine = BacktestEngine(10000)
    
    assert engine.portfolio_value(100) == 10000
    
def test_portfolio_value_with_open_position():
    engine = BacktestEngine(10000)
    
    engine.buy(100, 10)
    assert engine.portfolio_value(120) == 10200
    
def test_portfolio_value_after_multiple_trades():
    engine = BacktestEngine(10000)
    
    engine.buy(100, 10)
    engine.sell(120, 5)
    
    assert engine.portfolio_value(110) == 10150