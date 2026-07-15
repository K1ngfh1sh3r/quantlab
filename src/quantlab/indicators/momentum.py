import pandas as pd

def relative_strength_index(
    data: pd.DataFrame,
    column: str,
    window: int
) -> pd.Series:
    """
    calculates the Relative Strength Index (RSI)
    
    Args:
    data: pandas DataFrame containing market data
    column: Name of the Dataframe column on which the RSI is calculated 
    window: number of periods used to compute the relative strength
    
    Returns:
    A pandas Series containing the RSI
    
    Raises:
        ValueError:
            If window <= 0
            
        KeyError:
            If the requested column does not exist
    """
    if window <= 0:
        raise ValueError("window must be greater than 0")
    if column not in data.columns:
        raise KeyError(f"Column {column} does not exist")
    
    prices = data[column]
    
    delta = prices.diff()
    
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    
    avg_gain = gain.ewm(
        alpha=1/window,
        adjust=False
    ).mean()
    
    avg_loss = loss.ewm(
        alpha=1/window,
        adjust=False
    ).mean()
    
    rs = avg_gain / avg_loss.replace(0, float("nan"))
    
    rsi = 100 - (100/ (1 + rs))
    
    rsi.name = f"RSI_{column}"
    
    return rsi