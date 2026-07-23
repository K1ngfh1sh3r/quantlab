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
    def __init__(self,
                trade_type: str,
                price: float,
                quantity: int
        ) -> None:
        self.trade_type = trade_type
        self.price = price
        self.quantity = quantity
    
    @property
    def value(self):
        return self.price * self.quantity