from model.bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name: str, contact_number: str, balance: float, intereset_rate: float, min_balance: float):
        super().__init__(name, contact_number, balance)
        self.interest_rate = intereset_rate
        self.min_balance = min_balance

    def withdraw(self, amount: float):
        pass
