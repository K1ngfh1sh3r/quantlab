from quantlab.backtesting.trade import Trade

class Portfolio:
    """
    Represents a trading portfolio. 
    """    
    def __init__(self,
                 initial_capital: float
    ):
        if initial_capital <= 0:
            raise ValueError("Initial capital must be positive")
        
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.shares = 0
        self.trade_history: list[Trade] = []
        
    def value(self, 
            price: float
        ) -> float:
            return self.cash + (self.shares * price)
        
    def buy(self,
                price: float,
                quantity: int,
                commission: float = 1.50
                
        ) -> None :
            if price <= 0:
                raise ValueError("Price must be positive")
        
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
        
            if commission < 0:
                raise ValueError("Commission must be non-negative")
            
            cost = (price * quantity) + commission
            if cost > self.cash:
                raise ValueError("not enough cash")
            
            self.cash -= cost
            self.shares += quantity
            
            self.trade_history.append(
                Trade(
                    "BUY",
                    price,
                    quantity
                )
            )
            
    def sell(self,
                price: float,
                quantity: int,
                commission: float = 1.50
        ) -> None :
            if price <= 0:
                raise ValueError("Price must be positive")
        
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
            
            if quantity > self.shares:
                raise ValueError("Not enough shares")
            
            if commission < 0:
                raise ValueError("Commission must be non-negative")
                
            revenue = price * quantity
                
            self.cash += revenue - commission
            self.shares -= quantity
                
            self.trade_history.append(
                Trade(
                    "SELL",
                    price,
                    quantity
                )
            )