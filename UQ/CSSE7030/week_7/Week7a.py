class CreditAccount(object):
    """A simple credit account."""
    def __init__(self, owner, initial_deposit, monthly_interest, limit):
        self._owner = owner
        self._balance = initial_deposit
        self._interest = monthly_interest
        self._limit = limit
    def get_owner(self):
        return self._owner
    def get_balance(self):
        return self._balance
    def add_interest(self):
        """Add the monthly interest to the balance."""
        interest = self._balance * self._interest / 100.0
        self._balance += interest
    def deposit(self, amount):
        """Add the amount to the balance."""
        self._balance += amount
    def withdraw(self, amount):
        """Subtract the amount from the balance."""
        new_balance = self._balance - amount
        if new_balance < -self._limit:
            raise ValueError("Credit limit reached")
        else :
            self._balance = new_balance
    def __repr__(self):
        return "CreditAccount({0},{1},{2} {3})".format(self._owner,\
                            self._balance,self._interest,self._limit)

class SavingsAccount(object):
    """A simple savings account."""
    def __init__(self, owner, initial_deposit, monthly_interest):
        self._owner = owner
        self._balance = initial_deposit
        self._interest = monthly_interest
    def get_owner(self):
        return self._owner
    def get_balance(self):
        return self._balance
    def add_interest(self) :
        """Add the monthly interest to the balance."""
        interest = self._balance * self._interest / 100.0
        self._balance += interest
    def deposit(self, amount):
        """Add the amount to the balance."""
        self._balance += amount
    def withdraw(self, amount):
        """Subtract the amount from the balance."""
        new_balance = self._balance - amount
        if new_balance < 0:
            raise ValueError("Insufficient funds")
        else :
            self._balance = new_balance
    def __repr__(self) :
        return "SavingsAccount({0}, {1}, {2})".format(self._owner, self._balance,\
                                                self._interest)

