from account import Account

user = Account("Vyas", "1234", 1000)

def authenticate():
    for _ in range(3):
        pin = input("Enter PIN: ")
        if pin == user.pin:
            return True
        else:
            print("Incorrect PIN.")
    return False

def main():
    if not authenticate():
        print("Too many attempts. Card blocked.")
        return

    while True:
        print("\n1. Balance\n2. Deposit\n3. Withdraw\n4. History\n5. Exit")
        choice = input("Choose: ")
        if choice == '1':
            print(f"Balance: ₹{user.get_balance()}")
        elif choice == '2':
            amt = int(input("Amount: ₹"))
            user.deposit(amt)
        elif choice == '3':
            amt = int(input("Amount: ₹"))
            if not user.withdraw(amt):
                print("Insufficient Balance")
        elif choice == '4':
            print("\nTransaction History:")
            for h in user.get_history():
                print(" -", h)
        elif choice == '5':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice.")

main()
