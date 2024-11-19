class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            raise ValueError('Solo se peude trasnferir si es menor el monto al balance')
        return self.balance
            
        