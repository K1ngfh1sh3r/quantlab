from quantlab.backtesting.portfolio import Portfolio
from quantlab.backtesting.trade import Trade
import pytest

def test_portfolio_initialization():
    portfolio = Portfolio(10000)
    
    assert portfolio.initial_capital == 10000
    assert portfolio.cash == 10000
    assert portfolio.shares == 0
    assert portfolio.trade_history == []
    
def test_portfolio_value_without_position():
    portfolio = Portfolio(10000)
    
    assert portfolio.value(120) == 10000
    
def test_portfolio_value_with_position():
    portfolio = Portfolio(10000)
    
    portfolio.cash = 9500
    portfolio.shares = 5
    
    assert portfolio.value(120) == 10100
    
def test_buy_updates_cash():
    portfolio = Portfolio(10000)
    
    portfolio.buy(100,5)
    
    assert portfolio.cash == 9498.5
    
def test_buy_updates_shares():
    portfolio = Portfolio(10000)
        
    portfolio.buy(100,5)
        
    assert portfolio.shares == 5
    
def test_sell_updates_cash():
    portfolio = Portfolio(10000)
            
    portfolio.buy(100,5)
    portfolio.sell(120,2)
    
    assert portfolio.cash == 9737
    
def test_sell_updates_shares():
    portfolio = Portfolio(10000)
                
    portfolio.buy(100,5)
    portfolio.sell(120,2)
    
    assert portfolio.shares == 3
    
def test_sell_all_shares():
    portfolio = Portfolio(10000)

    portfolio.buy(100, 5)
    portfolio.sell(120, 5)

    assert portfolio.shares == 0
    assert portfolio.cash == 10097
    
def test_buy_adds_trade():
    portfolio = Portfolio(10000)

    portfolio.buy(100, 5)

    assert len(portfolio.trade_history) == 1
    assert isinstance(portfolio.trade_history[0], Trade)
    assert portfolio.trade_history[0].trade_type == "BUY"


def test_sell_adds_trade():
    portfolio = Portfolio(10000)

    portfolio.buy(100, 5)
    portfolio.sell(120, 2)

    assert len(portfolio.trade_history) == 2
    assert isinstance(portfolio.trade_history[1], Trade)
    assert portfolio.trade_history[1].trade_type == "SELL"


def test_buy_not_enough_cash():
    portfolio = Portfolio(100)

    with pytest.raises(ValueError):
        portfolio.buy(101, 1)


def test_sell_without_position():
    portfolio = Portfolio(10000)

    with pytest.raises(ValueError):
        portfolio.sell(100, 1)
        
def test_buy_all_cash():
    portfolio = Portfolio(10000)
    
    portfolio.buy(100,99)
    
    assert portfolio.cash == 98.5
    assert portfolio.shares == 99
    
def test_buy_invalid_quantity_zero():
    portfolio = Portfolio(10000)
    
    with pytest.raises(ValueError):
        portfolio.buy(100, 0)
        
def test_buy_invalid_quantity_negative():
    portfolio = Portfolio(10000)
    
    with pytest.raises(ValueError):
        portfolio.buy(100, -1)
        
def test_buy_negative_commission():
    portfolio = Portfolio(10000)
    
    with  pytest.raises(ValueError):
        portfolio.buy(100, 1, commission=-1)
        
def test_sell_invalid_quantity_zero():
    portfolio = Portfolio(10000)
    
    portfolio.buy(100, 5)
    
    with pytest.raises(ValueError):
        portfolio.sell(120, 0)
        
def test_sell_invalid_quantity_negative():
    portfolio = Portfolio(10000)
        
    portfolio.buy(100, 5)
        
    with pytest.raises(ValueError):
        portfolio.sell(120, -1)
        
def test_sell_too_many_shares():
    portfolio = Portfolio(10000)

    portfolio.buy(100, 5)

    with pytest.raises(ValueError):
        portfolio.sell(120, 6)


def test_sell_negative_commission():
    portfolio = Portfolio(10000)

    portfolio.buy(100, 5)

    with pytest.raises(ValueError):
        portfolio.sell(120, 1, commission=-1)


def test_buy_custom_commission():
    portfolio = Portfolio(10000)

    portfolio.buy(100, 5, commission=10)

    assert portfolio.cash == 9490
    assert portfolio.shares == 5


def test_sell_custom_commission():
    portfolio = Portfolio(10000)

    portfolio.buy(100, 5)
    portfolio.sell(120, 2, commission=10)

    assert portfolio.cash == 9728.5
    assert portfolio.shares == 3


def test_portfolio_value_after_trade():
    portfolio = Portfolio(10000)

    portfolio.buy(100, 5)

    assert portfolio.value(120) == 10098.5
    
def test_portfolio_zero_initial_capital():
    with pytest.raises(ValueError):
        Portfolio(0)

def test_portfolio_negative_initial_capital():
    with pytest.raises(ValueError):
        Portfolio(-1000)
        
def test_buy_zero_price():
    portfolio = Portfolio(10000)
    
    with pytest.raises(ValueError):
        portfolio.buy(0, 5)
        
def test_buy_negative_price():
    portfolio = Portfolio(10000)
    
    with pytest.raises(ValueError):
        portfolio.buy(-100, 5)
        
def test_sell_zero_price():
    portfolio = Portfolio(10000)
    
    portfolio.buy(100, 5)
    
    with pytest.raises(ValueError):
        portfolio.sell(0, 1)
        
def test_sell_negative_price():
    portfolio = Portfolio(10000)
    
    portfolio.buy(100, 5)
    
    with pytest.raises(ValueError):
        portfolio.sell(-100, 1)