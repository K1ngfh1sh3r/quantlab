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
    
    def summary(self) -> str:
        """
        Generate a readable performance summary.
        """
        return (
            f'Initial Capital: {self.statistics["initial_capital"]}\n'
            f'Final Value: {self.statistics["final_value"]}\n'
            f'Profit: {self.statistics["profit"]}\n'
            f'Return: {self.statistics["return_pct"]:.2f}%\n'
            f'Max Drawdown: {self.statistics["max_drawdown"]:.2f}%\n'
            f'Volatility: {self.statistics["volatility"]:.2f}%\n'
        )
        