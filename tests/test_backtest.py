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