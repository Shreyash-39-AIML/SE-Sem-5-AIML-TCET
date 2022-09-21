pin = int(input("Enter the ATM PIN: "))

balance = 10000
if pin == 1234:
    option = int(input("What would you like to do: \n1.Check Balance\n2.Withdraw\n3.Exit\nEnter Here: "))
    if option == 1:
        print(f"Your Account balance: {balance}")
    elif option == 2:
        amount = int(input("Enter Amount: "))
        balance -= amount
        print(f"Amount Withdrawn: {amount}")
        print(f"Remaining Account balance: {balance}")
    elif option == 3:
        print("Thank You")
else:
    print("Enter Correct Pin")
