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
    valid_type = ["BUY","SELL"]
    
    def __init__(self,
                trade_type: str,
                price: float,
                quantity: int
        ) -> None:
        
        if trade_type not in self.valid_type:
            raise ValueError("Invalid trade type")
        
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
    def value(self):
        return self.price * self.quantity