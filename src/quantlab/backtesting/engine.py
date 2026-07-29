import pandas as pd
from quantlab.backtesting.portfolio import Portfolio
from quantlab.strategies.base import Strategy

class BacktestEngine:
    """
    Basic backtesting engine.
    
    Run a trading strategy on historical market data
    """
    
    def __init__(
        self,
        initial_capital: float
    ):
        self.portfolio = Portfolio(initial_capital)
        self.last_price = None
    
    def run(self,
            data: pd.DataFrame,
            strategy: Strategy,
            price_column: str
        )-> pd.DataFrame:
        """
        Executes a backtest using trading signals.

        Args:
            data:
                DataFrame containing market data and signals.
                
            price_column:
                Column containing asset prices.

            strategy:
                Trading strategy used to generate signals.

        Returns:
            DataFrame containing portfolio evolution.
        """
        self.portfolio: Portfolio = Portfolio(
            self.portfolio.initial_capital
        )
        
        if price_column not in data.columns:
            raise KeyError(f"Column {price_column} does not exist")
        
        if not isinstance(strategy, Strategy):
            raise TypeError(
                "strategy must inherit from Strategy"
            )
        
        result = data.copy()
        
        portfolio_values: list[float] = []
        signals: list[int] = []
        
        for _, row in result.iterrows():
            
            price = row[price_column]
            self.last_price = price
            signal: int = strategy.generate_signal(row)
            
            signals.append(signal)
            
            if signal not in [-1,0,1]:
                raise ValueError("Invalid signal value")
            
            if signal == 1 and self.portfolio.shares == 0:
                self.portfolio.buy(price,1)
            
            elif signal == -1 and self.portfolio.shares > 0:
                self.portfolio.sell(price,1)
                
            portfolio_values.append(
                self.portfolio.value(price)
            )
            
            
        result["Signal"] = signals
        result["Portfolio_Value"] = portfolio_values
        
        return result
    
    def statistics(self):
        if self.last_price is None:
            raise ValueError("No backtest as been run yet")
        
        portfolio_value = self.portfolio.value(self.last_price)
        profit = portfolio_value- self.portfolio.initial_capital
        
        return {
            "initial_capital": self.portfolio.initial_capital,
            "final_value": portfolio_value,
            "profit": profit,
            "return_pct": (profit / self.portfolio.initial_capital) * 100
        }