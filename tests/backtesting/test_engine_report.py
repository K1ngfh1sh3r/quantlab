from quantlab.backtesting.engine import BacktestEngine
from quantlab.analytics.report import BacktestReport
from quantlab.strategies.buy_and_hold import BuyAndHoldStrategy

import pandas as pd
import pytest

def test_report_returns_backtest_report():
    data = pd.DataFrame({
        "Close": [100, 120, 110]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    report = engine.report()
    
    assert isinstance(report, BacktestReport)
    
def test_report_contains_statistics():
    data = pd.DataFrame({
        "Close": [100, 120, 110]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    report = engine.report()
    
    assert "return_pct" in report.statistics
    assert "max_drawdown" in report.statistics
    assert "volatility" in report.statistics
    assert "cagr" in report.statistics
    assert "sharpe_ratio" in report.statistics
    assert "sortino_ratio" in report.statistics

def test_report_without_run():
    engine = BacktestEngine(10000)
    
    with pytest.raises(ValueError):
        engine.report()
        
def test_report_get_value():
    data = pd.DataFrame({
        "Close": [100, 120, 110]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    report = engine.report()
    
    assert report.get("return_pct") == report.statistics["return_pct"]
    
def test_engine_report_contains_strategy_name():
    data = pd.DataFrame({
        "Close": [100, 120, 110]
    })

    engine = BacktestEngine(10000)

    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    report = engine.report()

    assert report.get_strategy_name() == "BuyAndHoldStrategy"