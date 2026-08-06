from quantlab.analytics.report import BacktestReport
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