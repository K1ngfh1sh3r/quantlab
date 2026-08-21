from quantlab.backtesting.engine import BacktestEngine
from quantlab.analytics.report import BacktestReport
from quantlab.strategies.buy_and_hold import BuyAndHoldStrategy

import pandas as pd
import pytest

def test_report_creation():
    stats = {
        "return_pct": 10,
        "volatility": 2
    }

    report = BacktestReport(stats)

    assert report.statistics == stats
    
def test_report_get_value():
    stats = {
        "return_pct": 10,
        "volatility": 2
    }
    
    report = BacktestReport(stats)
    
    assert report.get("return_pct") == 10
    
def test_report_invalid_key():
    stats = {
        "return_pct": 10,
        "volatility": 2
    }
    
    report = BacktestReport(stats)
    
    with pytest.raises(KeyError):
        report.get("unknown")
        
def test_report_invalid_statistics_type():
    with pytest.raises(TypeError):
        BacktestReport([])
        
def test_summary_returns_string():
    stats = {
        "initial_capital": 10000,
        "final_value": 15000,
        "profit": 5000,
        "return_pct": 50,
        "max_drawdown": 20,
        "volatility": 15
    }
    
    report = BacktestReport(stats)
    
    assert isinstance(report.summary(), str)
    
def test_summary_contains_metrics():
    stats = {
        "initial_capital": 10000,
        "final_value": 15000,
        "profit": 5000,
        "return_pct": 50,
        "max_drawdown": 20,
        "volatility": 15
    }
    
    report = BacktestReport(stats)
    summary = report.summary()
    
    assert "Initial Capital" in summary
    assert "Final Value" in summary
    assert "Profit" in summary
    assert "Return" in summary
    assert "Max Drawdown" in summary
    assert "Volatility" in summary
    
def test_report_plot_equity_curve(monkeypatch):
    data = pd.DataFrame({
        "Close": [100, 120, 110]
    })

    engine = BacktestEngine(10000)

    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    report = engine.report()

    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)

    result = report.plot_equity_curve()

    assert result is None

def test_report_plot_equity_curve_without_results():
    stats = {
        "return_pct": 10,
        "volatility": 2
    }

    report = BacktestReport(stats)

    with pytest.raises(ValueError):
        report.plot_equity_curve()

def test_report_contains_results():
    data = pd.DataFrame({
        "Close": [100, 120, 110]
    })

    engine = BacktestEngine(10000)

    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    report = engine.report()

    assert report.results is not None
    assert "Portfolio_Value" in report.results.columns

def test_report_plot_drawdown(monkeypatch):
    data = pd.DataFrame({
        "Close": [100, 120, 90]
    }) 
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    report = engine.report()
    
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)
    
    result = report.plot_drawdown()
    
    assert result is None
    
def test_report_available_plots():
    stats = {
        "return_pct": 10,
        "volatility": 2
    }
    
    report = BacktestReport(stats)
    
    assert report.available_plots() == [
        "equity_curve",
        "drawdown"
    ]
    
def test_report_plot(monkeypatch):
    data = pd.DataFrame({
        "Close": [100, 120, 90]
    })
    
    engine = BacktestEngine(10000)
    
    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )
    
    report = engine.report()
    
    equity_called = False
    drawdown_called = False
    
    def mock_equity_curve(_):
        nonlocal equity_called
        equity_called = True
        
    def mock_drawdown(_):
        nonlocal drawdown_called
        drawdown_called = True
        
    monkeypatch.setattr("quantlab.analytics.report.plot_equity_curve", mock_equity_curve)
    monkeypatch.setattr("quantlab.analytics.report.plot_drawdown", mock_drawdown)
    
    result = report.plot()
    
    assert result is None
    assert equity_called
    assert drawdown_called
    
def test_report_has_no_results():
    stats = {
        "return_pct": 10,
        "volatility": 2
    }
    
    report = BacktestReport(stats)
    
    assert report.has_results() is False
    
def test_report_has_results():
    stats = {
        "return_pct": 10,
        "volatility": 2
    }
    
    results = pd.DataFrame({
        "Portfolio_Value": [10000, 11000, 10500]
    })
    
    report = BacktestReport(stats, results)
    
    assert report.has_results() is True
    
def test_report_all_statistics():
    stats = {
        "return_pct": 10,
        "volatility": 2
    }
    
    report = BacktestReport(stats)
    
    result = report.all_statistics()
    
    assert result == stats
    assert result is not report.statistics
    
def test_report_contains_all_statistics():
    data = pd.DataFrame({
        "Close": [100, 120, 110, 130]
    })

    engine = BacktestEngine(10000)

    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    report = engine.report()

    expected_statistics = {
        "initial_capital",
        "final_value",
        "profit",
        "return_pct",
        "cagr",
        "max_drawdown",
        "volatility",
        "sharpe_ratio",
        "sortino_ratio",
    }

    assert expected_statistics.issubset(report.statistics.keys())
    
def test_report_all_statistics_contains_risk_metrics():
    data = pd.DataFrame({
        "Close": [100, 120, 110, 130]
    })

    engine = BacktestEngine(10000)

    engine.run(
        data,
        BuyAndHoldStrategy(),
        "Close"
    )

    report = engine.report()

    statistics = report.all_statistics()

    assert "cagr" in statistics
    assert "sharpe_ratio" in statistics
    assert "sortino_ratio" in statistics
    
def test_report_strategy_name():
    stats = {
        "return_pct": 10,
        "volatility": 2
    }

    report = BacktestReport(
        stats,
        strategy_name="TestStrategy"
    )

    assert report.get_strategy_name() == "TestStrategy"
    
def test_summary_contains_strategy_name():
    stats = {
        "initial_capital": 10000,
        "final_value": 11000,
        "profit": 1000,
        "return_pct": 10,
        "max_drawdown": 5,
        "volatility": 2
    }

    report = BacktestReport(
        stats,
        strategy_name="RSIStrategy"
    )

    summary = report.summary()

    assert "Strategy: RSIStrategy" in summary
    
def test_summary_without_strategy_name():
    stats = {
        "initial_capital": 10000,
        "final_value": 11000,
        "profit": 1000,
        "return_pct": 10,
        "max_drawdown": 5,
        "volatility": 2
    }

    report = BacktestReport(stats)

    summary = report.summary()

    assert "Strategy:" not in summary