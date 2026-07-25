import pytest
from quantlab.strategies.base import Strategy

def test_strategy_cannot_be_used():
    strategy = Strategy()
    
    with pytest.raises(NotImplementedError):
        strategy.generate_signal({})