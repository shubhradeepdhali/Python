from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance: int):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount : int):
        pass

    @abstractmethod
    def withdraw(self, amount : int):
        pass

    def view_balance(self)-> None:
        print(f"Your balance is {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, balance: int):
        super().__init__(balance)

    def withdraw(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            print("withdrawal successful")

    def deposit(self, amount: int):
        self.balance += amount
        print("deposit successful")

class FixedDeposit(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        raise Exception("Not valid")

    def deposit(self, amount: int):
        self.balance += amount
        print("amount deposited")


fixed_deposit_1 = FixedDeposit(5000)
savings_account_1 = SavingsAccount(7000)

fixed_deposit_1.deposit(700)
fixed_deposit_1.view_balance()

# fixed_deposit_1.withdraw(600)

savings_account_1.view_balance()