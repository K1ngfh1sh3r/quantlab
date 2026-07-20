from quantlab.backtesting.engine import BacktestEngine

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