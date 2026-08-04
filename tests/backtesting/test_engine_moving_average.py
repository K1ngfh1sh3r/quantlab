import pandas as pd
from quantlab.backtesting.engine import BacktestEngine
from quantlab.strategies.moving_average import MovingAverageStrategy

def test_engine_prepare_data_adds_sma():
    data = pd.DataFrame({
        "Close": [10, 20, 30, 40, 50, 60]
    })
    
    engine =  BacktestEngine(10000)
    
    result = engine.run(
        data,
        MovingAverageStrategy(2, 3),
        "Close"
    )
    
    assert "SMA_short" in result.columns
    assert "SMA_long" in result.columns
    
def test_engine_with_moving_average_returns_dataframe():
    data = pd.DataFrame({
            "Close": [10, 20, 30, 40, 50, 60]
        })
        
    engine =  BacktestEngine(10000)
        
    result = engine.run(
        data,
        MovingAverageStrategy(2, 3),
        "Close"
    )
    
    assert isinstance(result, pd.DataFrame)
    
def test_engine_with_moving_average_contains_backtest_columns():
    data = pd.DataFrame({
            "Close": [10, 20, 30, 40, 50, 60]
        })
        
    engine =  BacktestEngine(10000)
        
    result = engine.run(
        data,
        MovingAverageStrategy(2, 3),
        "Close"
    )
    
    assert "Signal" in result.columns
    assert "Portfolio_Value" in result.columns
    
def test_engine_calculates_sma_values():
    data = pd.DataFrame({
            "Close": [10, 20, 30, 40, 50, 60]
        })
        
    engine =  BacktestEngine(10000)
        
    result = engine.run(
        data,
        MovingAverageStrategy(2, 3),
        "Close"
    )
    
    assert result["SMA_short"].notna().sum() > 0
    assert result["SMA_long"].notna().sum() > 0
    
def test_engine_generates_signals():
    data = pd.DataFrame({
            "Close": [10, 20, 30, 40, 50, 60]
        })
        
    engine =  BacktestEngine(10000)
        
    result = engine.run(
        data,
        MovingAverageStrategy(2, 3),
        "Close"
    )
    
    assert any(signal != 0 for signal in result["Signal"])