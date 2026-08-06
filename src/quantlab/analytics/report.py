class BacktestReport:
    """
    Container for backtest analytics results.
    """
    
    def __init__(
        self,
        statistics: dict[str, float]
    ):
        if not isinstance(statistics, dict):
            raise TypeError("statistics must be a dictionary")
        
        self.statistics = statistics
        
    def get(self, key: str) -> float:
        """
        Return a statistic value
        """
        return self.statistics[key]
        