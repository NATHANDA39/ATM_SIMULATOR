
# Show Welcome message
print("WELCOME TO MEST ATM")
print("Please insert your atm card")
# Ask user to insert the card
user_card_name = input("Enter your name>> ") 
user_card_number = int(input("Enter your serial number>> "))
# Ask user to enter their pin
user_pin = 4190
current_balance = 10000.00

def pin_authentication():
    while True:
        pin = int(input("Enter your pin>> "))
        try:
            if pin == user_pin:
                print("Login Successful")
                break
            else:
                print("Authentication Failed")
                
        except ValueError:

            print("Invalid pin - Try again!")
    return pin        
    
pin_authentication()

def withdrawal():
    global current_balance
    amount = float(input("Enter the amount>> ")) 
    if amount <= 0:
        print("invalid input")
        
    if amount <= current_balance:
        current_balance -= amount
        print("withdrawal successful, please take your cash.")
    else:
        print("Insufficient balance")    

# Display options
def choices():
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Transaction History")
    print("5. Exit")

    options = input("Choose an option>> ")
    if options == "1":
        print(f"Your balance is Ghs {current_balance}")
    elif options == "2":
        print("Ready to Deposit") 
    elif options == "3":
        withdrawal()
    elif options == "4":
        print("History")  
    elif options == "5":
        print("Exit")
    else:
        print("Choose from the options")

choices()





