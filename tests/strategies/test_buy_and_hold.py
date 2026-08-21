from quantlab.strategies.buy_and_hold import BuyAndHoldStrategy


def test_buy_and_hold_initial_state():
    strategy = BuyAndHoldStrategy()

    assert strategy.position_open is False


def test_buy_and_hold_first_signal_is_buy():
    strategy = BuyAndHoldStrategy()

    signal = strategy.generate_signal({})

    assert signal == 1
    assert strategy.position_open is True


def test_buy_and_hold_subsequent_signal_is_hold():
    strategy = BuyAndHoldStrategy()

    strategy.generate_signal({})

    signal = strategy.generate_signal({})

    assert signal == 0


def test_buy_and_hold_keeps_position_open():
    strategy = BuyAndHoldStrategy()

    strategy.generate_signal({})

    for _ in range(10):
        assert strategy.generate_signal({}) == 0

    assert strategy.position_open is True