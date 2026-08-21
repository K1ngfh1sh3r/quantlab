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
        
def test_statistics_contains_sharpe_ratio():
    data = pd.DataFrame({
        "Close": [100, 110, 105, 120]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    stats = engine.statistics()
    
    assert "sharpe_ratio" in stats
    
def test_statistics_contains_sortino_ratio():
    data = pd.DataFrame({
            "Close": [100, 110, 105, 120]
    })
        
    engine = BacktestEngine(10000)
        
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
        
    stats = engine.statistics()
        
    assert "sortino_ratio" in stats
    
def test_statistics_cagr():
    data = pd.DataFrame(
        {
            "Close": [100, 120]
        },
        index=pd.to_datetime([
            "2024-01-01",
            "2025-01-01"
        ])
    )
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    stats = engine.statistics()
    
    expected_cagr = (10018.5 / 10000) ** (1 / (366 / 365.25)) - 1
    
    assert stats["cagr"] == pytest.approx(expected_cagr)
    
def test_statistics_cagr_without_datetime_index():
    data = pd.DataFrame({
        "Close": [100, 120]
    })
            
    engine = BacktestEngine(10000)
           
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    stats =engine.statistics()
    
    assert stats["cagr"] is None