class BankAccount:
    def __init__(self, name: str, contact_number: str, balance: float):
        self.name = name
        self.contact_number = contact_number
        self.__balance = balance

    def deposit(self, amount: float):
        pass

    def withdraw(self, amount: float):
        pass

    def show_balance(self):
        pass

    def show_history(self):
        pass