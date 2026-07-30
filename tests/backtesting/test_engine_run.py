from quantlab.backtesting.engine import BacktestEngine
from quantlab.strategies.buy_and_hold import BuyAndHoldStrategy
from quantlab.strategies.base import Strategy

import pandas as pd
import pytest


def test_run_returns_dataframe():

    data = pd.DataFrame({
        "Close": [100, 110, 120]
    })

    engine = BacktestEngine(10000)

    result = engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    assert isinstance(result, pd.DataFrame)


def test_run_contains_portfolio_value():

    data = pd.DataFrame({
        "Close": [100, 110, 120]
    })

    engine = BacktestEngine(10000)

    result = engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    assert "Portfolio_Value" in result.columns


def test_run_contains_signal():

    data = pd.DataFrame({
        "Close": [100, 110, 120]
    })

    engine = BacktestEngine(10000)

    result = engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    assert "Signal" in result.columns


def test_run_buy_and_hold_signal():

    data = pd.DataFrame({
        "Close": [100, 110, 120]
    })

    engine = BacktestEngine(10000)

    result = engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    assert result["Signal"].tolist() == [1, 0, 0]


def test_run_shares():

    data = pd.DataFrame({
        "Close": [100, 110, 120]
    })

    engine = BacktestEngine(10000)

    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    assert engine.portfolio.shares == 1


def test_run_trade_history():

    data = pd.DataFrame({
        "Close": [100, 110, 120]
    })

    engine = BacktestEngine(10000)

    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    assert len(engine.portfolio.trade_history) == 1
    assert engine.portfolio.trade_history[0].trade_type == "BUY"


def test_run_portfolio_value_calculation():

    data = pd.DataFrame({
        "Close": [100, 120]
    })

    engine = BacktestEngine(10000)

    result = engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    assert result["Portfolio_Value"].iloc[-1] == 10020


def test_run_invalid_price_column():

    data = pd.DataFrame({
        "Close": [100, 110]
    })

    engine = BacktestEngine(10000)

    with pytest.raises(KeyError):

        engine.run(
            data,
            BuyAndHoldStrategy(),
            "Price"
        )


def test_run_invalid_strategy():

    data = pd.DataFrame({
        "Close": [100, 110]
    })

    engine = BacktestEngine(10000)

    with pytest.raises(TypeError):
        engine.run(
            data,
            "not_a_strategy",
            "Close"
        )

def test_run_portfolio_evolution():

    data = pd.DataFrame({
        "Close": [100, 120, 130]
    })

    engine = BacktestEngine(10000)

    result = engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    assert result["Portfolio_Value"].iloc[0] == 10000
    assert result["Portfolio_Value"].iloc[1] == 10020
    assert result["Portfolio_Value"].iloc[2] == 10030
    
def test_run_empty_dataframe():
    
    data = pd.DataFrame({
        "Close": []
    })
    
    engine = BacktestEngine(10000)
    
    result = engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 0
    
class BadStrategy(Strategy):
    
    def generate_signal(self, row):
        return 5
    
def test_run_invalid_signal():
    data = pd.DataFrame({
        "Close": [100]
    })
    
    engine = BacktestEngine(10000)
    
    with pytest.raises(ValueError):
        engine.run(
            data,
            BadStrategy(),
            "Close"
        )
        
def test_statistics_returns_dict():
    data = pd.DataFrame({
        "Close": [100,120]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    stats = engine.statistics()
    
    assert isinstance(stats, dict)
    
def test_statistics_profit():
    data = pd.DataFrame({
            "Close": [100,120]
        })
        
    engine = BacktestEngine(10000)
        
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
        
    stats = engine.statistics()
    
    assert stats["profit"] == 20
    
def test_statistics_return():
    data = pd.DataFrame({
                "Close": [100,120]
            })
            
    engine = BacktestEngine(10000)
            
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
            
    stats = engine.statistics()
    
    assert stats["return_pct"] == 0.2
    
def test_statistics_final_value():
    data = pd.DataFrame({
                    "Close": [100,120]
                })
                
    engine = BacktestEngine(10000)
                
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
                
    stats = engine.statistics()
    
    assert stats["final_value"] == 10020
    
def test_run_quantity_buy():    
    data = pd.DataFrame({
            "Close": [100,120]
        })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close",
        quantity=5
    )
    
    assert engine.portfolio.shares == 5
    