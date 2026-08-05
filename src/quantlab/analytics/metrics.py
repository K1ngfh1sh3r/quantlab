import pandas as pd

def total_return(
    initial_value: float,
    final_value: float
) -> float:
    """
    Calculate the total portfolio return.

    Args:
        initial_value:
            Initial portfolio value.

        final_value:
            Final portfolio value.

    Returns:
        Total return expressed as a percentage.

    Raises:
        ValueError:
            If initial_value is less than or equal to zero.
    """
    if initial_value <= 0:
        raise ValueError("initial_value must be positive")
    
    return ((final_value - initial_value) / initial_value) * 100

def max_drawdown(
    portfolio_value: pd.Series
) -> float:
    """
    Calculate maximum portfolio drawdown.

    Args:
        portfolio_value:
            Historical portfolio values.

    Returns:
        Maximum drawdown expressed as percentage.

    Raises:
        ValueError:
            If portfolio_values is empty.
    """
    if portfolio_value.empty:
        raise ValueError("Portfolio_value must contain data")
    
    peak = portfolio_value.cummax()
    
    drawdown = ((portfolio_value - peak) / peak) * 100
    
    return drawdown.min()

def volatility(
    returns: pd.Series
) -> float:
    """
    Calculate portfolio volatility.

    Args:
        returns:
            Series containing portfolio returns.

    Returns:
        Volatility expressed as percentage.

    Raises:
        ValueError:
            If returns series is empty.
    """
    if returns.empty:
        raise ValueError("Returns must contain data")
    
    return returns.std() * 100