class BankAccount:
    def __init__(self, account_holder, initial_balance, pin):
        self.account_holder = account_holder  # Public attribute
        self._balance = initial_balance        # Protected attribute
        self.__pin = pin                       # Private attribute

    def get_balance(self):
        """Getter to retrieve the balance."""
        return self._balance

    def set_balance(self, amount):
        """Setter to update the balance (only if the amount is positive)."""
        if amount > 0:
            self._balance += amount
        else:
            print("Amount must be positive.")

    def verify_pin(self, pin):
        """Method to check if the entered PIN is correct."""
        return self.__pin == pin


# Demonstration of the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount("John Doe", 1000.0, "1234")

    # Accessing the public attribute
    print("Account Holder:", account.account_holder)

    # Trying to access the protected and private attributes
    print("Protected Balance (should be accessed carefully):", account._balance)
    try:
        print("Private PIN (should not be accessed directly):", account.__pin)
    except AttributeError as e:
        print("Error accessing private PIN:", e)

    # Using the getter and setter methods
    print("Current Balance:", account.get_balance())
    account.set_balance(500.0)  # Adding a positive amount
    print("Updated Balance:", account.get_balance())
    account.set_balance(-200.0)  # Trying to add a negative amount

    # Verifying the PIN
    pin_to_verify = "1234"
    if account.verify_pin(pin_to_verify):
        print("PIN verified successfully.")
    else:
        print("Incorrect PIN.")