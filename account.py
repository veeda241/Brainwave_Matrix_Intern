class Account:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew ₹{amount}")
            return True
        else:
            self.history.append(f"Failed Withdrawal ₹{amount}")
            return False

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.history
