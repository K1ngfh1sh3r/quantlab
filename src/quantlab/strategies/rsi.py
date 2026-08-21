import pandas as pd
from quantlab.indicators.momentum import relative_strength_index
from quantlab.strategies.base import Strategy

class RSIStrategy(Strategy):
    """
    RSI-based trading strategy

    Generates buy signals when the RSI is below the oversold threshold
    and sell signals when the RSI is above the overbought threshold
    """
    def __init__(
        self,
        window: int = 14,
        oversold: float = 30,
        overbought: float = 70
    ):
        if window <= 0:
            raise ValueError("Window must be positive")
        
        if not 0 <= oversold:
            raise ValueError("Oversold threshold must be between 0 and 100")
        
        if not 0 <= overbought <= 100:
            raise ValueError("Overbought threshold must be between 0 and 100")
        
        if oversold >= overbought:
            raise ValueError("Oversold threshold must be smaller than overbought threshold")
        
        self.window = window
        self.oversold = oversold
        self.overbought = overbought
        
    def prepare_data(
        self,
        data: pd.DataFrame,
        price_column: str = "Close"
    ) -> pd.DataFrame:
        """
        Add RSI values to market data.
        """
        result = data.copy()
        
        result["RSI"] = relative_strength_index(
            result,
            price_column,
            self.window
        )
        
        return result
    
    def generate_signal(self, row) -> int:
        """
        Generate trading signal based on RSI.

        Returns:
            1: Buy
            0: Hold
            -1: Sell
        """
        rsi = row["RSI"]
    
        if pd.isna(rsi):
            return 0
    
        if rsi < self.oversold:
            return 1
    
        if rsi > self.overbought:
            return -1
    
        return 0