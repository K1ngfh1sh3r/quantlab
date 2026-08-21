import pandas as pd
import pytest
from quantlab.strategies.rsi import RSIStrategy

def test_rsi_strategy_initialization():
    strategy = RSIStrategy()

    assert strategy.window == 14
    assert strategy.oversold == 30
    assert strategy.overbought == 70


def test_rsi_strategy_custom_parameters():
    strategy = RSIStrategy(
        window=10,
        oversold=25,
        overbought=75
    )

    assert strategy.window == 10
    assert strategy.oversold == 25
    assert strategy.overbought == 75


def test_rsi_strategy_invalid_window():
    with pytest.raises(ValueError):
        RSIStrategy(window=0)


def test_rsi_strategy_negative_window():
    with pytest.raises(ValueError):
        RSIStrategy(window=-1)


def test_rsi_strategy_invalid_oversold():
    with pytest.raises(ValueError):
        RSIStrategy(oversold=-1)

    with pytest.raises(ValueError):
        RSIStrategy(oversold=101)


def test_rsi_strategy_invalid_overbought():
    with pytest.raises(ValueError):
        RSIStrategy(overbought=-1)

    with pytest.raises(ValueError):
        RSIStrategy(overbought=101)


def test_rsi_strategy_invalid_threshold_order():
    with pytest.raises(ValueError):
        RSIStrategy(
            oversold=70,
            overbought=30
        )


def test_rsi_prepare_data_adds_rsi():
    data = pd.DataFrame({
        "Close": [100, 101, 102, 101, 100, 99, 100]
    })

    strategy = RSIStrategy(window=3)

    result = strategy.prepare_data(data)

    assert "RSI" in result.columns
    assert len(result) == len(data)


def test_rsi_prepare_data_does_not_modify_original_data():
    data = pd.DataFrame({
        "Close": [100, 101, 102, 101, 100]
    })

    strategy = RSIStrategy(window=3)

    strategy.prepare_data(data)

    assert "RSI" not in data.columns


def test_rsi_buy_signal():
    strategy = RSIStrategy(
        oversold=30,
        overbought=70
    )

    row = pd.Series({
        "RSI": 20
    })

    assert strategy.generate_signal(row) == 1


def test_rsi_sell_signal():
    strategy = RSIStrategy(
        oversold=30,
        overbought=70
    )

    row = pd.Series({
        "RSI": 80
    })

    assert strategy.generate_signal(row) == -1


def test_rsi_hold_signal():
    strategy = RSIStrategy(
        oversold=30,
        overbought=70
    )

    row = pd.Series({
        "RSI": 50
    })

    assert strategy.generate_signal(row) == 0


def test_rsi_nan_signal():
    strategy = RSIStrategy()

    row = pd.Series({
        "RSI": float("nan")
    })

    assert strategy.generate_signal(row) == 0


def test_rsi_boundary_oversold():
    strategy = RSIStrategy(
        oversold=30,
        overbought=70
    )

    row = pd.Series({
        "RSI": 30
    })

    assert strategy.generate_signal(row) == 0


def test_rsi_boundary_overbought():
    strategy = RSIStrategy(
        oversold=30,
        overbought=70
    )

    row = pd.Series({
        "RSI": 70
    })

    assert strategy.generate_signal(row) == 0