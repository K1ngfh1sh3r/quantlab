import yfinance as yf
from datetime import date
import pandas

def download_market_data(
    ticker:str,
    start:date,
    end:date
    ) -> pandas.DataFrame :
    """
    Download historical market data
    
    Args:
    ticker: Financial instrument symbol.
    start: Beginning date.
    end: Ending date.

    Returns:
    Historical OHLCV market data.
    """
    market_data = yf.download(
        tickers=ticker,
        start=start,
        end=end,
        progress=False)
    
    if market_data.columns.nlevels > 1:
        market_data.columns = market_data.columns.droplevel(1)
    return market_data