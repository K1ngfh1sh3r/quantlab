import pandas as pd

from quantlab.strategies.base import Strategy
from quantlab.indicators.moving_average import simple_moving_average


class MovingAverageStrategy(Strategy):
    """
    Moving average crossover strategy.

    Generates buy and sell signals based on
    short and long moving average crossover.
    """
    
    def __init__(self,
                short_window: int,
                long_window: int
                ):
        
        if short_window <= 0:
            raise ValueError("Short window must be positive")
        
        if long_window <= 0:
            raise ValueError("Long window must be positive")
        
        if short_window >= long_window:
            raise ValueError("Short window must be smaller than long window")
        
        self.short_window = short_window
        self.long_window = long_window
        
    def prepare_data(self,
                    data: pd.DataFrame,
                    price_column: str = "Close"
                ) -> pd.DataFrame:
        """
        Add moving average to market data
        """
        
        result = data.copy()
        
        result["SMA_short"] = simple_moving_average(
            result,
            price_column,
            self.short_window
        )
        
        result["SMA_long"] = simple_moving_average(
            result,
            price_column,
            self.long_window
        )
        
        return result
    
    def generate_signal(self,
                        row
                    ) -> int:
        """
        Generate trading signal.

        Returns:
            1: Buy
            0: Hold
           -1: Sell
        """
        if pd.isna(row["SMA_short"]) or pd.isna(row["SMA_long"]):
            return 0
        
        if row["SMA_short"] > row["SMA_long"]:
            return 1
        
        if row["SMA_short"] < row["SMA_long"]:
            return -1
        
        return 0