import matplotlib.pyplot as plt
import pandas as pd

def plot_drawdown(
    portfolio_value: pd.Series
) -> None:
    """
    Plot the portfolio drawdown.

    Args:
        portfolio_value:
            Historical portfolio values.

    Raises:
        ValueError:
            If portfolio_value is empty.
    """
    if portfolio_value.empty:
        raise ValueError("Portfolio value must contain data")
    
    running_max = portfolio_value.cummax()
    drawdown = (portfolio_value - running_max) / running_max
    
    plt.figure()
    plt.plot(drawdown)
    plt.title("Portfolio Drawdown")
    plt.xlabel("Period")
    plt.ylabel("Drawdown")
    plt.grid(True)
    plt.show()