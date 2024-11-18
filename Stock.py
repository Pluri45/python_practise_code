# A Stock object represents purchases of shares of a stock.
class Stock:
    # Initializes a new Stock with no shares purchased.
    def __init__(self, symbol):
        self._symbol = symbol  # stock symbol, e.g. "YHOO"
        self._total_shares = 0  # total shares purchased
        self._total_cost = 0.0  # total cost for all shares

    # Read-only properties to access Stock's state.
    @property
    def symbol(self):
        return self._symbol

    @property
    def total_cost(self):
        return self._total_cost
    

    @property
    def total_shares(self):
        return self._total_shares
    
    @total_cost.setter
    def total_cost(self, value):
        self._total_cost= value
        
    @total_shares.setter
    def total_shares(self, value ):
        self._total_shares = value 
        
    @symbol.setter
    def symbol(self, value ):
        self._symbol  =  value  
            
    

    # Returns the total profit or loss earned on this stock,
    # based on the given price per share.
    # pre: current_price >= 0.0
    def profit(self, current_price):
        if current_price < 0.0:
            raise ValueError("Current price cannot be negative")
        return self._total_shares * current_price - self._total_cost

    # Records purchase of the given shares at the given price.
    # pre: shares >= 0 && price_per_share >= 0.0
    def purchase(self, shares, price_per_share):
        if shares < 0 or price_per_share < 0.0:
            raise ValueError("Shares/price cannot be negative")
        self._total_shares += shares
        self._total_cost += shares * price_per_share
        
    def clear(self):
        self._total_shares = 0  
        self._total_cost = 0.0 
        return  self._total_shares , self._total_cost 
        