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

    assert result["Portfolio_Value"].iloc[-1] == 10018.5


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

    assert result["Portfolio_Value"].iloc[0] == 9998.5
    assert result["Portfolio_Value"].iloc[1] == 10018.5
    assert result["Portfolio_Value"].iloc[2] == 10028.5

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
    
    assert stats["profit"] == 18.5
    
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
    
    assert stats["return_pct"] == 0.185
    
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
    
    assert stats["final_value"] == 10018.5
    
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

def test_run_quantity_cash():
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
    
    assert engine.portfolio.cash == 9498.5
    
def test_run_quantity_zero():
    data = pd.DataFrame({
                "Close": [100,120]
            })
            
    engine = BacktestEngine(10000)
    
    with pytest.raises(ValueError):
        engine.run(
            data,
            BuyAndHoldStrategy(),
            "Close",
            quantity=0
        )
        
def test_run_quantity_negative():
    data = pd.DataFrame({
                    "Close": [100,120]
                })
                
    engine = BacktestEngine(10000)
        
    with pytest.raises(ValueError):
        engine.run(
            data,
            BuyAndHoldStrategy(),
            "Close",
            quantity=-1
        )
        
def test_run_commission_buy():
    data = pd.DataFrame({
            "Close": [100,120]
        })
                    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close",
        commission=10
    )
    
    assert engine.portfolio.cash == 9890
    
def test_run_negative_quantity():
    data = pd.DataFrame({
            "Close": [100]
        })
                    
    engine = BacktestEngine(10000)
    
    with pytest.raises(ValueError):
        
        engine.run(
            data,
            BuyAndHoldStrategy(),
            "Close",
            quantity=-1
        )

def test_run_negative_commission():
    data = pd.DataFrame({
        "Close": [100]
    })
    
    engine = BacktestEngine(10000)
    
    with pytest.raises(ValueError):
        
        engine.run(
            data,
            BuyAndHoldStrategy(),
            "Close",
            commission=-1
        )
        
def test_export_csv_creates_file(tmp_path):
    data = pd.DataFrame({
        "Close": [100, 120]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    filename = tmp_path / "results.csv"
    
    engine.export_csv(filename)
    
    assert filename.exists()
    
def test_export_csv_without_run():
    engine = BacktestEngine(10000)
    
    with pytest.raises(ValueError):
        engine.export_csv("results.csv")
        
def test_export_csv_contains_columns(tmp_path):
    data = pd.DataFrame({
        "Close": [100, 120]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    filename = tmp_path / "results.csv"
    
    engine.export_csv(filename)
    
    exported = pd.read_csv(filename)
    
    assert "Signal" in exported.columns
    assert "Portfolio_Value" in exported.columns 
    
def test_export_csv_rows():
    data = pd.DataFrame({
            "Close": [100, 120, 130]
        })
        
    engine = BacktestEngine(10000)
        
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    engine.export_csv("test.csv")
    
    exported = pd.read_csv("test.csv")
    
    assert len(exported) == 3
    
def test_statistics_without_run():
    engine = BacktestEngine(10000)
    
    with pytest.raises(ValueError):
        engine.statistics()

def test_report_without_run():
    engine  =BacktestEngine(10000)
    
    with pytest.raises(ValueError):
        engine.report()
        
def test_run_single_row():
    data = pd.DataFrame({
        "Close": [100]
    })
    
    engine = BacktestEngine(10000)
    
    result = engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    assert len(result) == 1
    assert result["Signal"].iloc[0] == 1
    assert engine.portfolio.shares == 1
    
def test_run_invalid_data_type():
    engine = BacktestEngine(10000)
    
    with pytest.raises(TypeError):
        engine.run(
            [100, 110, 120],
            BuyAndHoldStrategy(),
            "Close"
        )
        
def test_run_empty_dataframe_raises():
    data = pd.DataFrame({
        "Close": []
    })
    
    engine = BacktestEngine(10000)
    
    with pytest.raises(ValueError):
        engine.run(
            data,
            BuyAndHoldStrategy(),
            "Close"
        )

def test_engine_invalid_initial_capital():
    with pytest.raises(ValueError):
        BacktestEngine(0)
        
def test_engine_negative_initial_capital():
    with pytest.raises(ValueError):
        BacktestEngine(-1000)
        
def test_run_invalid_quantity_type():
    data = pd.DataFrame({
        "Close": [100, 120]
    })
    
    engine =BacktestEngine(10000)
    
    with pytest.raises(TypeError):
        engine.run(
            data,
            BuyAndHoldStrategy(),
            "Close",
            quantity="1"
        )
        
def test_run_invalid_commission_type():
    data = pd.DataFrame({
        "Close": [100, 120]
    })
    
    engine = BacktestEngine(10000)
    
    with pytest.raises(TypeError):
        engine.run(
            data,
            BuyAndHoldStrategy(),
            "Close",
            commission="1.5"
        )
        
def test_run_nan_price():
    data = pd.DataFrame({
        "Close": [100, float("nan"), 120]
    })

    engine = BacktestEngine(10000)

    with pytest.raises(ValueError):
        engine.run(
            data,
            BuyAndHoldStrategy(),
            "Close"
        )


def test_run_zero_price():
    data = pd.DataFrame({
        "Close": [100, 0, 120]
    })

    engine = BacktestEngine(10000)

    with pytest.raises(ValueError):
        engine.run(
            data,
            BuyAndHoldStrategy(),
            "Close"
        )


def test_run_negative_price():
    data = pd.DataFrame({
        "Close": [100, -10, 120]
    })

    engine = BacktestEngine(10000)

    with pytest.raises(ValueError):
        engine.run(
            data,
            BuyAndHoldStrategy(),
            "Close"
        )