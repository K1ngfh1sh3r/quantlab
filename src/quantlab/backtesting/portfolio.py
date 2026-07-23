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
        
    def value(self, 
                            price: float
            ) -> float:
            return self.cash + (self.shares * price)
        
    def buy(self,
                price: float,
                quantity: int
        ) -> None :
            cost = price * quantity
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
                quantity: int
        ) -> None :
            if quantity > self.shares:
                raise ValueError("Not enough shares")
                
            revenue = price * quantity
                
            self.cash += revenue
            self.shares -= quantity
                
            self.trade_history.append(
                Trade(
                    "SELL",
                    price,
                    quantity
                )
            )