import pandas as pd

def total_return(
    portfolio_value: pd.Series
) -> float:
    """
    Calculate total return percentage.

    Args:
        portfolio_values:
            Portfolio value evolution.

    Returns:
        Total return in percentage.
    """
    initial_value = portfolio_value.iloc[0]
    final_value = portfolio_value.iloc[-1]
    
    return ((final_value - initial_value) / initial_value) * 100

def daily_returns(
    portfolio_value: pd.Series
) -> pd.Series:
    """
    Calculate daily returns
    """
    return portfolio_value.pct_change().dropna()

def max_drawdown(
    portfolio_value: pd.Series
) -> float:
    """
    Calculate maximum drawdown percentage.
    """
    peak = portfolio_value.cummax()
    
    drawdown = ((portfolio_value - peak) / peak) * 100
    
    return drawdown.min()