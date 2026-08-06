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
        
