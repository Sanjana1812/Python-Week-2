class BankAccount:

    def __init__(self, account_number, holder_name, balance):    # store account details
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):                            # add amount to balance
        self.balance = self.balance + amount
        print("Amount Deposited Successfully")

    def withdraw(self, amount):                    # withdraw only if balance is enough

        if amount > self.balance:
            print("Insufficient Balance")

        else:
            self.balance = self.balance - amount
            print("Withdrawal Successful")

    def check_balance(self):                        # show current balance
        print("Current Balance :", self.balance)



account = BankAccount(101, "San", 5000)     # Creating account object

while True:

    print("\n----- BANK MENU -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter Choice: "))             # taking menu choice

    if choice == 1:                                    # user enters deposit amount

        amount = float(input("Enter Amount: "))         # user enters withdraw amount
        account.deposit(amount)

    elif choice == 2:

        amount = float(input("Enter Amount: "))
        account.withdraw(amount)

    elif choice == 3:

        account.check_balance()

    elif choice == 4:

        print("Thank You")
        break

    else:
        print("Invalid Choice")
