import pytest
from quantlab.strategies.base import Strategy
from quantlab.strategies.buy_and_hold import BuyAndHoldStrategy

def test_strategy_generate_signal_is_not_implemented():
    strategy = Strategy()

    with pytest.raises(NotImplementedError):
        strategy.generate_signal({})
        
def test_strategy_name():
    strategy = Strategy()
    
    assert strategy.name() == "Strategy"
    
def test_buy_and_hold_strategy_name():
    strategy = BuyAndHoldStrategy()
    
    assert strategy.name() == "BuyAndHoldStrategy"