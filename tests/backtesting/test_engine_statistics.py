from quantlab.backtesting.engine import BacktestEngine
from quantlab.strategies.buy_and_hold import BuyAndHoldStrategy
import pandas as pd
import pytest

def test_statistics_returns_dict():
    data = pd.DataFrame({
        "Close": [100, 120, 110]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    stats = engine.statistics()
    
    assert isinstance(stats, dict)
    
def test_statistics_contains_analytics_metrics():
    data = pd.DataFrame({
            "Close": [100, 120, 110]
        })
        
    engine = BacktestEngine(10000)
        
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
        
    stats = engine.statistics()
    
    assert "max_drawdown" in stats
    assert "volatility" in stats
    
def test_statistics_max_drawdown():
    data = pd.DataFrame({
            "Close": [100, 120, 90]
        })
        
    engine = BacktestEngine(10000)
        
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
        
    stats = engine.statistics()
    
    assert stats["max_drawdown"] <= 0
    
def test_statistics_volatility_positive():
    data = pd.DataFrame({
            "Close": [100, 120, 90, 130]
        })
        
    engine = BacktestEngine(10000)
        
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
        
    stats = engine.statistics()
    
    assert stats["volatility"] > 0
    
def test_statistics_metrics_are_float():
    data = pd.DataFrame({
            "Close": [100, 120, 90, 130]
        })
        
    engine = BacktestEngine(10000)
        
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
        
    stats = engine.statistics()
    
    assert isinstance(stats["max_drawdown"], float)
    assert isinstance(stats["volatility"], float)
    
def test_statistics_without_run():
    engine = BacktestEngine(10000)
    
    with pytest.raises(ValueError):
        engine.statistics()