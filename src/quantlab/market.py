import yfinance as yf
from datetime import date


help(yf.download)
def download_market_data(ticker:str,start:date,end:date):
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
    
    return market_data