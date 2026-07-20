from quantlab.backtesting.engine import BacktestEngine

def test_backtest_initial_capital():
    engine = BacktestEngine(10000)
    
    assert engine.initial_capital == 10000
    assert engine.cash == 10000
    assert engine.shares == 0
    assert engine.trade_history == []