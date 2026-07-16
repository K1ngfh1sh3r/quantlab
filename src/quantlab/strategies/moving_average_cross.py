import pandas as pd
import numpy as np
from quantlab.indicators.moving_average import simple_moving_average

def moving_average_crossover(
    data: pd.DataFrame,
    column: str,
    short_window: int,
    long_window: int
) -> pd.DataFrame :
    """
    Generates trading signals based on a moving average crossover strategy.

    The strategy compares a short-term moving average with a long-term
    moving average to generate trading signals.

    Signal convention:
        1:
            Buy signal / Long position.
            The short moving average is above the long moving average.

        0:
            Hold / No position.
            No crossover signal is detected.

        -1:
            Sell signal / Exit position.
            The short moving average is below the long moving average.

    Args:
        data:
            DataFrame containing market data.
            Must contain a price column used for the moving averages.
            
        column:
            Name of the column used to compute the moving averages.

        short_window:
            Number of periods used for the short-term moving average.

        long_window:
            Number of periods used for the long-term moving average.

    Returns:
        A DataFrame containing the original market data,
        moving averages and generated trading signals.

    Raises:
        ValueError:
            If windows are <= 0 or if short_window >= long_window.

        KeyError:
            If the required price column does not exist.
    """
    if short_window <= 0 or long_window <= 0:
        raise ValueError("window must be greater than 0")
    if short_window >= long_window:
        raise ValueError("short_window must be smaller than long_window")
    if column not in data.columns:
        raise KeyError(f"Column {column} does not exist")
    
    short_ma = simple_moving_average(data, column, short_window)
    long_ma = simple_moving_average(data, column, long_window)
    
    result = data.copy()
    
    result["Short_MA"] = short_ma
    result["Long_MA"] = long_ma
    
    result["Signal"] = np.where(
        short_ma > long_ma, 
        1,
        np.where(
            short_ma < long_ma,
            -1,
            0
        )
    )
    
    return result
