from model.bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, name: str, contact_number: str, balance: float, withdrawal_fee: float):
        super().__init__(name, contact_number, balance)
        self.withdrawal_fee = withdrawal_fee

    def withdraw(self, amount: float):
        pass
