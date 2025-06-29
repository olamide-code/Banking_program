#PYTHON BANKING PROGRAM

def show_balance():
    print(f"Your balance is: ${balance: .2f}")

def deposit():
    amount = float(input("How much do you want to deposit: "))
    if amount < 0:
        print("You cannot deposit negative amount")
        return None

    else:
        return amount
def withdraw():
    pass

balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice(1-4):")

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance+=deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("invalid choice")

