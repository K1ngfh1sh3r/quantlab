import pandas as pd

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
    ) -> None :
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
    ) -> None :
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
        
    def portfolio_value(self, 
                        price: float
        ) -> float:
        return self.cash + (self.shares * price)
    
    def run(self,
            data: pd.DataFrame,
            price_column: str,
            signal_column: str
        )-> pd.DataFrame:
        """
        Executes a backtest using trading signals.

        Args:
            data:
                DataFrame containing market data and signals.
                
            price_column:
                Column containing asset prices.

            signal_column:
                Column containing trading signals.

        Returns:
            DataFrame containing portfolio evolution.
        """
        result = data.copy()
        
        portfolio_values = []
        
        for _, row in result.iterrows():
            
            price = row[price_column]
            signal = row[signal_column]
            
            if signal == 1:
                self.buy(price,1)
            
            elif signal == -1:
                self.sell(price,1)
                
            portfolio_values.append(
                self.portfolio_value(price)
            )
            
        result["Portfolio_Value"] = self.portfolio_values
        
        return result