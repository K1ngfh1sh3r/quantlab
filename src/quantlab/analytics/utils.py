import pandas as pd

def calculate_returns(
    portfolio_values: pd.Series 
) -> pd.Series:
    """
    Calculate period returns from portfolio values.

    Args:
        portfolio_values:
            Historical portfolio values.

    Returns:
        Pandas Series containing percentage returns.

    Raises:
        ValueError:
            If portfolio_value is empty.
    """
    if portfolio_values.empty:
        raise ValueError("Portfolio_values must contain data")
        
    return portfolio_values.pct_change()