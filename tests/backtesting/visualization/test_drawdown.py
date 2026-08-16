
from quantlab.visualization.drawdown import plot_drawdown
import matplotlib.pyplot as plt
import pandas as pd
import pytest

def test_plot_drawdown_with_valid_data(monkeypatch):
    portfolio_value = pd.Series([
        10000,
        12000,
        9000,
        11000
    ])
    
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)
    
    plot_drawdown(portfolio_value)
    
def test_plot_drawdown_empty_series():
    portfolio_value = pd.Series([], dtype=float)
    
    with pytest.raises(ValueError):
        plot_drawdown(portfolio_value)
        
def test_plot_drawdown_returns_none(monkeypatch):
    portfolio_value = pd.Series([
        10000,
        12000,
        9000
    ])

    monkeypatch.setattr(
        "matplotlib.pyplot.show",
        lambda: None
    )

    result = plot_drawdown(portfolio_value)

    assert result is None


def test_plot_drawdown_creates_plot(monkeypatch):
    portfolio_value = pd.Series([
        10000,
        12000,
        9000,
        11000
    ])

    monkeypatch.setattr(
        "matplotlib.pyplot.show",
        lambda: None
    )

    plot_drawdown(portfolio_value)

    figure = plt.gcf()

    assert len(figure.axes) == 1
    assert len(figure.axes[0].lines) == 1


def test_plot_drawdown_uses_portfolio_values(monkeypatch):
    portfolio_value = pd.Series([
        10000,
        12000,
        9000,
        11000
    ])

    monkeypatch.setattr(
        "matplotlib.pyplot.show",
        lambda: None
    )

    plot_drawdown(portfolio_value)

    figure = plt.gcf()
    line = figure.axes[0].lines[0]

    assert line.get_ydata()[-1] == pytest.approx(-1 / 12)