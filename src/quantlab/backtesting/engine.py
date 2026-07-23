import pandas as pd
from quantlab.backtesting.portfolio import Portfolio

class BacktestEngine:
    """
    Basic backtesting engine.
    """
    
    def __init__(
        self,
        initial_capital: float
    ):
        self.portfolio = Portfolio(initial_capital)
    
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
        self.portfolio = Portfolio(
            self.portfolio.initial_capital
        )
        
        if price_column not in data.columns:
            raise KeyError(f"Column {price_column} does not exist")
        
        if signal_column not in data.columns:
            raise KeyError(f"Column {signal_column} does not exist")
        
        result = data.copy()
        
        portfolio_values = []
        
        for _, row in result.iterrows():
            
            price = row[price_column]
            signal = row[signal_column]
            
            if signal not in [-1,0,1]:
                raise ValueError("Invalid signal value")
            
            if signal == 1 and self.portfolio.shares == 0:
                self.portfolio.buy(price,1)
            
            elif signal == -1 and self.portfolio.shares > 0:
                self.portfolio.sell(price,1)
                
            portfolio_values.append(
                self.portfolio.value(price)
            )
            
        result["Portfolio_Value"] = portfolio_values
        
        return result