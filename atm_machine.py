option = 0
balance = 5000
pin = 1234

def driver_code(option):
    if option == 1:
        check_balance()
    elif option == 2:
        withdraw()
    elif option == 3:
        transfer()
    elif option == 4:
        deposit()
    elif option == 5:
        change_pin()
    elif option == 6:
        print("Thanks for using the ATM Machine\nHave a Great Day\n")
        exit(0)


def aunthenticate():
    counter = 1
    while counter < 4:
        try:
            mypin = int(input("Please enter your PIN: "))
        except:
            print("PIN is a Four Digit Number , not a String\n")
            main_menu()

        if mypin == pin:
            print("Welcome\nCorrect PIN\n")
            counter = 1
            global option
            driver_code(option)
        
        elif mypin != pin:
            print(f"\nYou have entered {counter} time Wrong PIN\nWarning: After Three Wrong Attempt you will be Terminated")
        counter+=1


def check_balance():
    print("Your available Balance is: ", balance)  
    exit(0)

def withdraw():
    global balance
    try:
        withdraw_money = int(input("How much Money you want to Withdraw: "))
    except:
        print("Enter valid amount of Money")
        main_menu()

    if withdraw_money > balance:  
        print("Not enough Balance")
        check_balance()
    else:
        print("Please collect your Cash\nThanks for visiting the ATM\nHave a Great Day")
        balance = balance - withdraw_money
        check_balance()

def transfer():
    global balance
    try:
        ac_number = int(input("Enter the Account Number: "))
        ifsc_code = input("Enter the IFSC Code: ")
    except:
        print("Invalid Account Number Entered")
        driver_code()

    try:
        trans_money = int(input("How much Money you want to Transfer: "))
    except:
        print("Invalid Amount of Money Entered!!!")
        driver_code()

    if trans_money > balance:
        print("Insufficient Fund in your Account")
        check_balance()
    else:
        print(f"Succesfully Transfered {trans_money} to {ac_number} Account Number\nThanks for visiting the ATM")
        balance = balance - trans_money
        check_balance()


def deposit():
    try:
        dep_money = int(input("How much money you want to Deposit: "))
    except:
        print("Not a Valid Amount of Money")
        driver_code()

    global balance
    balance = balance + dep_money
    print("Money Deposited Successfully")
    check_balance()


def change_pin():
    global pin
    try:
        new_pin = int(input("Enter the new four digit PIN: "))
    except:
        print("Enter a Valid PIN Type")
        change_pin()

    if len(str(new_pin)) != 4:
        print("PIN should be only of Four Digits")
        change_pin()
    
    else:
        pin = new_pin
        print("Your PIN changed Successfully")
        exit(0)


def main_menu():
    print("\n***** Welcome to the ATM Machine *****")
    print('''
    1: Check Balance
    2: Withdraw Money
    3: Transfer Money
    4: Deposit Money
    5: Change PIN
    6: Exit
    ''')

    global option
    try:
        option = int(input("Select an Option: "))    
    except:
        print("Invalid Option")
        main_menu()
    
    if option<1 or option>6:
        print("Entered Option is not Valid!!\nPlease select a valid Option")
        main_menu()


if __name__=='__main__':
    main_menu()
    aunthenticate()