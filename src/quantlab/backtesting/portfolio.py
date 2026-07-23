from quantlab.backtesting.trade import Trade

class Portfolio:
    """
    Represents a trading portfolio. 
    """    
    def __init__(self,
                 initial_capital: float
    ):
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.shares = 0
        self.trade_history: list[Trade] = []
        
        