class BacktestEngine:
    """
    Basic backtesting engine.
    """
    
    def __init__(
        self,
        initial_capital: float
    ):
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.shares = 0
        self.trade_history = []
        
    def buy(self,
            price: float,
            quantity: int
    ):
        cost = price * quantity
        if cost > self.cash:
            return ValueError("not enough cash")