from typing import ClassVar

class Trade:
    """
    Represents a single executed trade.

    A trade stores the information related to one buy or sell
    transaction executed during a backtest.

    Attributes:
        trade_type:
            Type of trade ("BUY" or "SELL").

        price:
            Execution price of the trade.

        quantity:
            Number of shares traded.
    """
    VALID_TYPES: ClassVar[list[str]] = ["BUY", "SELL"]
    
    def __init__(self,
                trade_type: str,
                price: float,
                quantity: int
        ) -> None:
        
        if trade_type not in self.VALID_TYPES:
            raise ValueError("Invalid trade type")
        
        if price <= 0:
            raise ValueError("Price must be positive")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        self.trade_type = trade_type
        self.price = price
        self.quantity = quantity
        
    def is_buy(self) -> bool:
        return self.trade_type == "BUY"
    
    def is_sell(self) -> bool:
        return self.trade_type == "SELL"
    
    @property
    def value(self) -> float:
        return self.price * self.quantity