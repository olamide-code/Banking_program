#PYTHON BANKING PROGRAM

def show_balance(balance):
    print(f"Your balance is: ${balance: .2f}")

def deposit():
    amount = float(input("How much do you want to deposit: "))
    if amount < 0:
        print("You cannot deposit negative amount")
        return None

    else:
        return amount
def withdraw():
    amount = float(input("How much do you want to withdraw:"))
    if amount > balance:
        print("You cannot withdraw more than your balance")
        return None
    elif amount < 0:
        print("You cannot withdraw negative amount")
        return None
    else:
        return amount


    balance = 0
    is_running = True

while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ")

    if choice == "1":
        show_balance(balance)
    elif choice == "2":
        balance+=deposit()
    elif choice == "3":
        balance-= withdraw(balance)
    elif choice == "4":
        is_running = False
    else:
        print("invalid choice")

print("Thank you for Banking with us")

