import pandas as pd
from quantlab.visualization.equity_curve import plot_equity_curve
from quantlab.visualization.drawdown import plot_drawdown


class BacktestReport:
    """
    Container for backtest analytics results.
    """

    def __init__(
        self,
        statistics: dict[str, float],
        results: pd.DataFrame | None = None,
        strategy_name: str | None = None
    ):
        if not isinstance(statistics, dict):
            raise TypeError("statistics must be a dictionary")

        self.statistics = statistics
        self.results = results
        self.strategy_name = strategy_name
        
    def has_results(self) -> bool:
        """
        Return whether backtest results are available.
        """
        return self.results is not None

    def get(self, key: str) -> float:
        """
        Return a statistic value
        """
        return self.statistics[key]
    
    def all_statistics(self) -> dict[str, float]:
            """
            Return all backtest statistics
            """
            return self.statistics.copy()

    def summary(self) -> str:
        """
        Generate a readable performance summary.
        """
        strategy_line = ""
        
        if self.strategy_name is not None:
            strategy_line = f"Strategy: {self.strategy_name}\n"
        
        return (
            strategy_line
            + f'Initial Capital: {self.statistics["initial_capital"]}\n'
            + f'Final Value: {self.statistics["final_value"]}\n'
            + f'Profit: {self.statistics["profit"]}\n'
            + f'Return: {self.statistics["return_pct"]:.2f}%\n'
            + f'Max Drawdown: {self.statistics["max_drawdown"]:.2f}%\n'
            + f'Volatility: {self.statistics["volatility"]:.2f}%\n'
        )

    def plot_equity_curve(self) -> None:
        """
        Plot the portfolio equity curve.
        """
        if self.results is None:
            raise ValueError("No backtest results available")

        if "Portfolio_Value" not in self.results.columns:
            raise KeyError("Portfolio_Value column does not exist")

        plot_equity_curve(self.results["Portfolio_Value"])
        
    def plot(self) -> None:
        """
        Plot the available backtest visualizations
        """
        self.plot_equity_curve()
        self.plot_drawdown()
        
    def available_plots(self) -> list[str]:
        """
        Return the available backtest visualizations
        """
        return [
            "equity_curve",
            "drawdown"
        ]
    
    def plot_drawdown(self) -> None:
        """
        Plot the portfolio drawdown.
        """
        if self.results is None:
            raise ValueError("No backtest results available")
        
        if "Portfolio_Value" not in self.results.columns:
            raise KeyError("Portfolio_Value column does not exist")
        
        plot_drawdown(self.results["Portfolio_Value"])
        
    def get_strategy_name(self) -> str | None:
        """
        Return the name of the strategy used for the backtest.
        """
        return self.strategy_name
