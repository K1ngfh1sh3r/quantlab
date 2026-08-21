class Strategy:
    """
    Base class for all strategies
    
    Every strategy must implement the generate_signal() method
    """
    
    def generate_signal(self,row) -> int:
        """
        Returns:
            -1 : sell
             0 : hold
             1 : buy 
        """
        raise NotImplementedError
    
    def name(self) -> str:
        """
        Return the strategy name
        """
        return self.__class__.__name__