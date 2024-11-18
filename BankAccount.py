# Each BankAccount object represents one user's account
# information including name and balance of money.
class BankAccount:
    def __init__(self, name):
        self._name = name
        self._balance = 0.0  
        self._transaction_fee = 0.0  
        
    def __str__(self):
        return str( self._name ) + ", " + str( self._balance ) 
        
    
    @property 
    def name(self):
        return self._name
    @property 
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance_setter(self, value):
        self._balance += value
    @property 
    def transaction_fee(self):
        return  self._transaction_fee
        
    @transaction_fee.setter
    def transaction_fee(self, value):
        if value < 0:
            raise ValueError("Transaction fee cannot be negative")
        self._transaction_fee= value

    def _deposit(self, amount):
        if amount > 0:
             self._balance += amount
        else:     
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
          amount = amount +self._transaction_fee
          if 0 < amount <= self._balance:
            self._balance -=  amount
          else:     
            raise ValueError("  withdraw amount must be positive")
        
    def transfer(self, other_bank_account, amount):
       transaction_fee = 5.0       
       transfer_amount = amount + transaction_fee
       
       if  amount <= 0:
           print("Transfer amount must be positive")
           return
       if self._balance < 5:
            return "No transaction occurred"
       if self._balance > transfer_amount: 
           self._balance-=  transfer_amount 
           other_bank_account.balance += amount
   
       else:
           # Partial transfer: only transfer what remains after deducting fee
            transfer_amount = self._balance - transaction_fee
            other_bank_account.balance_setter(transfer_amount)
