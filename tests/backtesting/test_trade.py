import pytest

from quantlab.backtesting.trade import Trade


def test_trade_creation():
    trade = Trade(
        "BUY",
        100,
        5
    )

    assert trade.trade_type == "BUY"
    assert trade.price == 100
    assert trade.quantity == 5


def test_trade_buy():
    trade = Trade(
        "BUY",
        100,
        5
    )

    assert trade.is_buy()
    assert not trade.is_sell()


def test_trade_sell():
    trade = Trade(
        "SELL",
        120,
        10
    )

    assert trade.is_sell()
    assert not trade.is_buy()


def test_trade_value():
    trade = Trade(
        "BUY",
        100,
        5
    )

    assert trade.value == 500


def test_trade_sell_value():
    trade = Trade(
        "SELL",
        120,
        10
    )

    assert trade.value == 1200


def test_trade_invalid_type():
    with pytest.raises(ValueError):
        Trade(
            "HOLD",
            100,
            5
        )


def test_trade_empty_type():
    with pytest.raises(ValueError):
        Trade(
            "",
            100,
            5
        )


def test_trade_zero_quantity():
    with pytest.raises(ValueError):
        Trade(
            "BUY",
            100,
            0
        )


def test_trade_negative_quantity():
    with pytest.raises(ValueError):
        Trade(
            "BUY",
            100,
            -1
        )
        
def test_trade_zero_price():
    with pytest.raises(ValueError):
        Trade(
            "BUY",
            0,
            5
        )
        
def test_trade_negative_price():
    with pytest.raises(ValueError):
        Trade(
            "BUY",
            -100,
            5
        )