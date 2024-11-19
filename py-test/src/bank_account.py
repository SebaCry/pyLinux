class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')
        self._log_transaction_fail('Lo sentimos, no tienes fondos suficientes')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f'{message}\n') 

    def _log_transaction_fail(self, message):
        if self.log_file:    
            with open(self.log_file, "a") as f:
                f.write(f'{message}\n')

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f'Deposited {amount}. New balance: {self.balance}')
        return self.balance
    
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f'Deposited {amount}. New balance: {self.balance}')
        return self.balance
    
    def get_balance(self):
        self._log_transaction(f'Checked balance. New balance: {self.balance}')
        return self.balance
    
    def transfer(self, amount):
        if amount > self.balance:
            self._log_transaction('Intento fallido de transferencia')
            raise ValueError('Solo se puede transferir si es menor el monto al balance')
        self.balance -= amount
        self._log_transaction('Transferencia realizada')
        return self.balance
    

        