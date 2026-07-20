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
            raise ValueError("not enough cash")
        
        self.cash -= cost
        self.shares += quantity
        
        self.trade_history.append(
            {
                "type": "BUY",
                "price": price,
                "quantity": quantity
            }
        )
        
    def sell(self,
            price: float,
            quantity: int
    ):
        if quantity > self.shares:
            raise ValueError("Not enough shares")
        
        revenue = price * quantity
        
        self.cash += revenue
        self.shares -= quantity
        
        self.trade_history.append(
            {
                "type": "SELL",
                "price": price,
                "quantity": quantity
            }
        )
        
    def portfolio_value(self, price: float):
        return self.cash + (self.shares * price)