import matplotlib.pyplot as plt
import pandas as pd

def plot_equity_curve(
    portfolio_value: pd.Series
) -> None:
    """
    Plot the portfolio equity curve.

    Args:
        portfolio_value:
            Historical portfolio values.

    Raises:
        ValueError:
            If portfolio_value is empty.
    """
    if portfolio_value.empty:
        raise ValueError("Portfolio value must contain data")
    plt.figure()
    plt.plot(portfolio_value)
    plt.title("Portfolio Equity Curve")
    plt.xlabel("Period")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.show()