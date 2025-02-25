#!/usr/bin/env python
# coding: utf-8

# In[1]:


accounts = {
    1001: [1000, 2408, "user1@gmail.com", "user1"],
    1002: [2000, 1234, "user2@gmail.com", "user2"],
    1003: [10000, None, "user3@gmail.com", "user3"]
}

print("Welcome to the Bank!")
while True:
    print("\n*******************************")
    print("Choose your Option: ")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini Statement")
    print("5. Exit")
    
    try:
        x = int(input("Enter Your Option: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1-5.")
        continue

    print("********************************")
    
    if x == 1:  # Withdraw
        print("********** Withdraw **********")
        try:
            acc = int(input("Enter Your Account Number: "))
            if acc not in accounts:
                print("Invalid Account Number")
                continue

            if accounts[acc][1] is None:
                print(f"Dear {accounts[acc][3]}, PIN Not Generated!")
                continue

            pin = int(input("Enter your PIN: "))
            if accounts[acc][1] == pin:
                amt = int(input("Enter Amount to Withdraw: "))
                if amt <= 0:
                    print("Invalid Amount! Enter a positive number.")
                elif accounts[acc][0] >= amt:
                    accounts[acc][0] -= amt
                    print("Amount Withdrawn Successfully!")
                else:
                    print("Insufficient Balance")
            else:
                print("Invalid PIN!")
        except ValueError:
            print("Invalid Input! Please enter numbers only.")
        print("********************************")

    elif x == 2:  # Deposit
        print("********** Deposit **********")
        try:
            acc = int(input("Enter Your Account Number: "))
            if acc not in accounts:
                print("Invalid Account Number")
                continue

            amt = int(input("Enter Amount to Deposit: "))
            if amt <= 0:
                print("Invalid Amount! Enter a positive number.")
            else:
                accounts[acc][0] += amt
                print("Deposit Successful!")
        except ValueError:
            print("Invalid Input! Please enter numbers only.")
        print("********************************")

    elif x == 3:  # PIN Generation
        print("********** PIN Generation **********")
        try:
            acc = int(input("Enter Your Account Number: "))
            if acc not in accounts:
                print("Invalid Account Number")
                continue

            if accounts[acc][1] is not None:
                print("PIN Already Generated!")
            else:
                pin = int(input("Enter New PIN (4 Digits): "))
                if 1000 <= pin <= 9999:
                    accounts[acc][1] = pin
                    print("PIN Generated Successfully!")
                else:
                    print("Invalid PIN! Please enter a 4-digit number.")
        except ValueError:
            print("Invalid Input! Please enter numbers only.")
        print("********************************")

    elif x == 4:  # Mini Statement
        print("********** Mini Statement **********")
        try:
            acc = int(input("Enter Your Account Number: "))
            if acc not in accounts:
                print("Invalid Account Number")
                continue

            pin = int(input("Enter your PIN: "))
            if accounts[acc][1] == pin:
                print(f"Name: {accounts[acc][-1]}")
                print(f"Email: {accounts[acc][-2]}")
                print(f"Balance: ₹{accounts[acc][0]}")
            else:
                print("Invalid PIN!")
        except ValueError:
            print("Invalid Input! Please enter numbers only.")
        print("********************************")

    elif x == 5:  # Exit
        print("*****************************")
        print("Thank You for Banking with Us!")
        print("Visit Again")
        print("*****************************")
        break

    else:
        print("Invalid Option! Please enter a number between 1-5.")


# In[ ]:





# In[5]:





# In[ ]:






