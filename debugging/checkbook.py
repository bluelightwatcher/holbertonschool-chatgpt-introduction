#!/usr/bin/python3
class Checkbook:
    """
    A simple Checkbook class to track deposits, withdrawals, and the balance.

    Attributes:
        balance (float): The current balance of the checkbook.

    Methods:
        deposit(amount: float) -> None:
            Adds the specified amount to the balance and prints a confirmation.
        
        withdraw(amount: float) -> None:
            Deducts the specified amount from the balance if sufficient funds are available.
            If insufficient funds, it prints an error message.
        
        get_balance() -> None:
            Prints the current balance.
    """

    def __init__(self):
        """
        Initializes the Checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the specified amount into the checkbook and updates the balance.

        Parameters:
            amount (float): The amount to be deposited.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the checkbook if sufficient funds exist.
        If there are insufficient funds, it prints an error message.

        Parameters:
            amount (float): The amount to be withdrawn.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook class. Provides options for the user
    to deposit money, withdraw money, view the current balance, or exit the program.

    The program runs in a loop until the user chooses to exit. User input is case-insensitive.

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()

        if action == 'exit':
            break  # Exit the loop and end the program

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

