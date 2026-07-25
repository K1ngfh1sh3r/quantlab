from quantlab.strategies.base import Strategy

class BuyAndHoldStrategy(Strategy):
    """
    Simple buy and hold strategy

    Buys the asset on the first signal
    and keeps the position open
    """
    
    
    def __init__(self):
        self.position_open = False
        
    def generate_signal(self, row) -> int:
        
        if not self.position_open:
            self.position_open = True
            return 1

        return 0