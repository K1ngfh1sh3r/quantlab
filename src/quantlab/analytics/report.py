import pandas as pd

from quantlab.visualization.equity_curve import plot_equity_curve


class BacktestReport:
    """
    Container for backtest analytics results.
    """

    def __init__(
        self,
        statistics: dict[str, float],
        results: pd.DataFrame | None = None
    ):
        if not isinstance(statistics, dict):
            raise TypeError("statistics must be a dictionary")

        self.statistics = statistics
        self.results = results

    def get(self, key: str) -> float:
        """
        Return a statistic value.
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

    def plot_equity_curve(self) -> None:
        """
        Plot the portfolio equity curve.
        """
        if self.results is None:
            raise ValueError("No backtest results available")

        if "Portfolio_Value" not in self.results.columns:
            raise KeyError("Portfolio_Value column does not exist")

        plot_equity_curve(self.results["Portfolio_Value"])