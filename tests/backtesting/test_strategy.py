import pytest
from quantlab.strategies.base import Strategy
from quantlab.strategies.buy_and_hold import BuyAndHoldStrategy

def test_strategy_cannot_be_used():
    strategy = Strategy()
    
    with pytest.raises(NotImplementedError):
        strategy.generate_signal({})
        
def test_first_signal_is_buy():
    strategy = BuyAndHoldStrategy()
    
    assert strategy.generate_signal({}) == 1

def test_second_signal_is_hold():
    strategy = BuyAndHoldStrategy()
    
    strategy.generate_signal({})
    
    assert strategy.generate_signal({}) == 0

def test_buy_and_hold_never_sells():
    strategy = BuyAndHoldStrategy()
        
    signals = [
        strategy.generate_signal({}),
        strategy.generate_signal({}),
        strategy.generate_signal({}),
        strategy.generate_signal({})
    ]
        
    assert -1 not in signals