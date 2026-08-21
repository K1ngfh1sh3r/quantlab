import pandas as pd
from quantlab.backtesting.engine import BacktestEngine
from quantlab.strategies.rsi import RSIStrategy


def test_engine_runs_rsi_strategy():
    data = pd.DataFrame(
        {
            "Close": [
                100, 98, 96, 94, 92,
                90, 92, 95, 98, 100,
                102, 100, 97, 94, 91
            ]
        }
    )

    engine = BacktestEngine(10000)

    result = engine.run(
        data,
        RSIStrategy(window=3),
        "Close"
    )

    assert "RSI" in result.columns
    assert "Signal" in result.columns
    assert "Portfolio_Value" in result.columns


def test_engine_rsi_strategy_generates_signals():
    data = pd.DataFrame(
        {
            "Close": [
                100, 98, 96, 94, 92,
                90, 92, 95, 98, 100
            ]
        }
    )

    engine = BacktestEngine(10000)

    result = engine.run(
        data,
        RSIStrategy(
            window=3,
            oversold=30,
            overbought=70
        ),
        "Close"
    )

    assert set(result["Signal"].unique()).issubset({-1, 0, 1})


def test_engine_rsi_strategy_produces_portfolio_values():
    data = pd.DataFrame(
        {
            "Close": [
                100, 98, 96, 94, 92,
                90, 92, 95, 98, 100
            ]
        }
    )

    engine = BacktestEngine(10000)

    result = engine.run(
        data,
        RSIStrategy(window=3),
        "Close"
    )

    assert result["Portfolio_Value"].notna().all()
    assert len(result) == len(data)