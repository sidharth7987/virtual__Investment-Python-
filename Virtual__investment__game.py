def Axis_Bank():
    Bank_Name = "Axis Bank"
    Risk_Type = "Very High Risk"
    Rating = "3.8"
    Minimum_amount = 100
    Past_Year_Return = "15%"
    Interest_Rate = 0.05
    return (
        f"Bank Name: {Bank_Name}\n"
        f"Risk Type: {Risk_Type}\n"
        f"Rating: {Rating}\n"
        f"Minimum Amount: {Minimum_amount}\n"
        f"Past Year Return: {Past_Year_Return}\n"
        f"Interest Rate: {Interest_Rate * 100}%"
    )

def return_amount_Axis_Bank(Investment_Amount):
    Interest_Rate = 0.05
    return Investment_Amount*Interest_Rate

def HDFC_Bank():
    Bank_Name = "HDFC Bank"
    Risk_Type = "ModeratelyHigh Risk"
    Rating = "4.2"
    Minimum_amount = 100
    Past_Year_Return = "10%"
    Interest_Rate = 0.03
    return (
        f"Bank Name: {Bank_Name}\n"
        f"Risk Type: {Risk_Type}\n"
        f"Rating: {Rating}\n"
        f"Minimum Amount: {Minimum_amount}\n"
        f"Past Year Return: {Past_Year_Return}\n"
        f"Interest Rate: {Interest_Rate * 100}%"
    )

def return_amount_HDFC_Bank(Investment_Amount):
    Interest_Rate = 0.03
    return Investment_Amount*Interest_Rate

Initial_Balance = 1000

while True:
    User_input = input("What do you want?  'Withdraw Money', 'Check Balance', 'Investment' or 'done to exit'  ")

    if User_input == "Withdraw Money":
        Withdrawal_amount = int(input("How much amount you want to withdraw?  "))
        if Withdrawal_amount < 100 or Withdrawal_amount > Initial_Balance:
            print("Please Enter a vaild Amount.")
        else:
            Initial_Balance -= Withdrawal_amount
            print("Withdrawl Amount", Withdrawal_amount)
            print("Balance", Initial_Balance)

    elif User_input == "Check Balance":
        print("Current Balance: ", Initial_Balance)  

    elif User_input == "Investment":
        print(Axis_Bank())

        print("----------------------------------------------------------")
        
        print(HDFC_Bank())
        
        Investment_Amount = float(input("How Much amount do you want to Invest?  "))

        if Investment_Amount < 100:
            print("Minimum Investment is 100")
            print("Please Enter a valid amount")
        elif Investment_Amount > Initial_Balance:
            print("You don't have enough balance for this investment.")
            
        else:
            User_Bank = input("In which Bank do you want to Invest Your Money? '1 for Axis Bank' or '2 for HDFC Bank'   ")
            if User_Bank == "1":
                return_amount = return_amount_Axis_Bank(Investment_Amount)
                print("Investment Amount: ", Investment_Amount)
                print(f"Return Amount from Axis Bank: {return_amount}")

            elif User_Bank == "2":
                return_amount = return_amount_HDFC_Bank(Investment_Amount)
                print("Investment Amount: ", Investment_Amount)
                print(f"Return Amount from HDFC Bank: {return_amount}") 

            else:
                print("Invalid bank choice.")
                continue
            
            Initial_Balance -= Investment_Amount
            print("Balance after investment:", Initial_Balance)

    elif User_input == "done":
        print("Thankyou! 🙂")
        break

    else:
        print("Invalid option. Please try again.")