class WithdrawalError(Exception) :
    """An exception to be raised when a withdrawal fails."""
    def __init__(self, message, balance) :
        """
        Parameters
            message (str): The reason for the error
            balance (float): The balance of the account 
        """
        super().__init__(message)
        self._balance = balance

    def get_balance(self) :
        return self._balance



class SavingsAccount(object) :
    """A simple savings account."""
    def __init__(self, owner, initial_deposit, monthly_interest) :
        self._owner = owner
        self._balance = initial_deposit
        self._interest = monthly_interest

    def get_owner(self) :
        return self._owner

    def get_balance(self) :
        return self._balance

    def add_interest(self) :
        """Add the monthly interest to the balance."""
        if self._balance > 0 :
            interest = self._balance * self._interest / 100.0
            self._balance += interest

    def deposit(self, amount) :
        """Add a positive amount to the balance."""
        if amount < 0 :
            raise ValueError("Can't deposit a negative amount")
        self._balance += amount

    def withdraw(self, amount) :
        """Subtract a positive amount from the balance."""
        if amount < 0 :
            raise ValueError("Can't withdraw a negative amount")
        
        new_balance = self._balance - amount
        if new_balance < 0 :
            raise WithdrawalError("Not enough funds in account", self._balance)
        else :
            self._balance = new_balance

    def __repr__(self) :
        repr_string = "SavingsAccount({0}, {1}, {2})"
        return repr_string.format(self._owner, self._balance, self._interest)



def withdraw(account, amount) :
    try :
        account.withdraw(amount)
    except ValueError as e :
        print("Invalid:", e)
    except WithdrawalError as e :
        print("Cannot withdraw:", e)
        print("Your account balance is ${0}".format(e.get_balance()))
    else :
        print("Withdrawal successful.")



def deposit(account, amount) :
    try :
        account.deposit(amount)
    except ValueError as e :
        print("Invalid:", e)
    else :
        print("Deposit successful.")
