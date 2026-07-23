from quantlab.backtesting.trade import Trade
import pytest
from quantlab.backtesting.engine import BacktestEngine

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
    
    engine.portfolio.buy(100, 5)
    
    assert isinstance(engine.trade_history[0], Trade)
    
def test_trade_return():
    engine = BacktestEngine(10000)
    
    engine.portfolio.buy(100, 5)
    
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
    
def test_trade_invalid_type():
    with pytest.raises(ValueError):
        Trade(
            "HOLD",
            100,
            5
        )
        
        
def test_trade_invalid_quantity():
    with pytest.raises(ValueError):
        Trade(
            "BUY",
            100,
            -5
        )
        
def test_trade_is_buy():
    trade = Trade(
        "BUY",
        100,
        5
    )
    
    assert trade.is_buy()
    assert not trade.is_sell()
    
def test_trade_is_sell():
    trade = Trade(
        "SELL",
        120,
        5
    )
    
    assert trade.is_sell()
    assert not trade.is_buy()