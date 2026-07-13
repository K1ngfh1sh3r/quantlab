import pandas as pd

def simple_moving_average(
    data: pd.DataFrame,
    column: str,
    window: int,
) -> pd.Series: 
    """
    calculates the Simple Moving Average (SMA)
    
    Args:
    data: pandas DataFrame containing market data
    column: Name of the Dataframe column on which the SMA is calculated 
    window: number of periods used to compute the moving average
    
    Returns:
    A pandas Series containing the SMA
    
    Raises:
        ValueError:
            If window <= 0
            
        KeyError:
            If the requested column does not exist
    """
    if window <= 0:
        raise ValueError()
    if column not in data.columns:
        raise KeyError()
    
    prices = data[column]
    sma = prices.rolling(window).mean()
    
    return sma