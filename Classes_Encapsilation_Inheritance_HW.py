#Mitchel Bechtold
#11/4/2025
#Classes, Encapsulation, Inheritance Homework

# Part 1
# BankAccount and SavingsAccount

class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return self._balance
        else:
            print("Error: Deposit amount must be positive.")
            return self._balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            print("Insufficient funds.")
            return self._balance

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"Account {self.account_number} - Owner: {self.owner} - Balance: ${self._balance:.2f}"

# SavingsAccount (inherits from BankAccount)

class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, initial_balance, interest_rate):
        # Call parent constructor to set up base attributes
        super().__init__(account_number, owner, initial_balance)
        self.interest_rate = interest_rate  # e.g. 0.02 for 2%

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest

    def withdraw(self, amount):
        if self._balance - amount < 100:
            print("Cannot go below $100 minimum")
            return self._balance
        else:
            return super().withdraw(amount)

# Test the classes
if __name__ == "__main__":
    # Regular account
    regular = BankAccount("1001", "Alice", 500)
    print(regular)
    regular.deposit(100)
    print(f"After deposit: ${regular.balance}")
    regular.withdraw(200)
    print(f"After withdrawal: ${regular.balance}")

    print("\n" + "="*40 + "\n")

    # Savings account
    savings = SavingsAccount("2001", "Bob", 1000, 0.02)
    print(savings)
    interest = savings.add_interest()
    print(f"Interest earned: ${interest:.2f}")
    print(f"New balance: ${savings.balance}")
    # Try to go below minimum
    savings.withdraw(950)  # Should fail
    savings.withdraw(500)  # Should work
    print(f"Final balance: ${savings.balance}")

