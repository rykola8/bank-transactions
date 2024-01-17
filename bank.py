# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# 

transactions = []

def deposit(transactions, amount):
    transactions.append(amount)

def withdraw(transactions, amount):
    transactions.append(amount * -1)

def check_balance(transactions):
    sum = 0
    for i in transactions:
        sum += i
    if sum < 0:
        print("You're in debt: " + str(sum))
    elif sum > 0:
        print(sum)

def list(transactions):
    print(transactions)

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. List transactions")
    print("5. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("How much do you want to add to the bill?: "))
        deposit(transactions, amount)
        print(transactions)
    elif choice == '2':
         amount = float(input("How much do you want to remove from the bill?: "))
         withdraw(transactions, amount)
         print(transactions)
    elif choice == '3':
        check_balance(transactions)
    elif choice == '4':
        print(transactions)
    elif choice == '5':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
