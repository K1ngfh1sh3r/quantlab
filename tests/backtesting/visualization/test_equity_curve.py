import matplotlib.pyplot as plt
import pandas as pd
import pytest

from quantlab.visualization.equity_curve import plot_equity_curve

def test_plot_equity_curve_with_valid_data(monkeypatch):
    portfolio_value = pd.Series([
        10000,
        10500,
        10200,
        11000
    ])
    
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)
    
    plot_equity_curve(portfolio_value)
    
def test_plot_equity_curve_empty_series():
    portfolio_value = pd.Series([], dtype=float)
    
    with pytest.raises(ValueError):
        plot_equity_curve(portfolio_value)
        
def test_plot_equity_curve_returns_none(monkeypatch):
    portfolio_value = pd.Series([
        10000,
        10500,
        11000
    ])
    
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)
    
    result = plot_equity_curve(portfolio_value)
    
    assert result is None
    
def test_plot_equity_curve_creates_plot(monkeypatch):
    portfolio_value = pd.Series([
        10000,
        10500,
        10200,
        11000
    ])
    
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)
    
    plot_equity_curve(portfolio_value)
    
    figure = plt.gcf()
    axes = figure.axes
    
    assert len(axes) == 1
    assert len(axes[0].lines) == 1
    
def test_plot_equity_curve_uses_portfolio_values(monkeypatch):
    portfolio_value = pd.Series([
        10000,
        10500,
        10200,
        11000
    ])

    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)

    plot_equity_curve(portfolio_value)

    figure = plt.gcf()
    line = figure.axes[0].lines[0]

    assert list(line.get_ydata()) == portfolio_value.tolist()