class BankAccount:
    def __init__(self,account_number,holder_name,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("Deposit Successful")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            print("Withdrawal successful")
    
    def display_balance(self):
        print("Current Balance:", self.balance)
        
acc_no=input("enter account number:")
name=input("Enter account holder name:")
balance=float(input("Enter balance:"))

account=BankAccount(acc_no,name,balance)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Display Balance\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        amt = float(input("Enter deposit amount: "))
        account.deposit(amt)

    elif choice == '2':
        amt = float(input("Enter withdrawal amount: "))
        account.withdraw(amt)

    elif choice == '3':
        account.display_balance()

    elif choice == '4':
        print("Thank you!")
        break

    else:
        print("Invalid choice")