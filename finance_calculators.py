"""this program provides an investement calculator and a home loan repayment calculator"""

import math

#provide two calculator options to the user 
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n"
      "\n"
      "investment   - to calculate the amount of interest you'll earn on interest \n"
      "bond         - to calculate the amount you'll have to pay on a home loan \n"
      " ")

#store choice and convert to lowercase letters to avoid errors
user_choice = input()
user_choice = user_choice.lower()

#if-statement to test user choice and display error message if invalid choice
if user_choice != "investment" and user_choice != "bond":
    print("You have entered an invalid choice! Please restart.")

#if-statement for the investment calculator    
if user_choice == "investment":

    #user provides data to be used in calculation
    deposit = float(input("Please enter deposit amount: R "))
    interest_rate = float(input("Please enter the interest rate percentage: ")) / 100
    investment_term = float(input("Please enter the number of years you are investing for: "))
    interest_type = input("Do you prefer simple or compound interest? (simple/compound)")

    #convert interest choice to lower case to avoid errors
    interest_type = interest_type.lower()

    #nested if-statements for interest choice calculations using given formula
    if interest_type == "simple":
        total_amount = round(deposit * (1 + interest_rate * investment_term), 2)

    if interest_type == "compound":
        total_amount = round(deposit * math.pow((1 + interest_rate), investment_term), 2)

    #display total amount
    print("The total amount of your investment with the interest applied is: R {}".format(total_amount))

#if-statement for the bond calculator
if user_choice == "bond":

    #user provides data to be used in calculation
    house_value = float(input("Please enter the present value of the house R: "))
    monthly_interest_rate = (float(input("Please enter the interest rate percentage: ")) / 100) / 12
    investment_term = float(input("Please enter the number of months you are taking the repay bond: "))

    #bond repayment calculations using given formula
    total_monthly_repayment = round(((monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** ( -investment_term ))), 2)

    #display total monthly repayment
    print("The total monthly repayment is: R {}".format(total_monthly_repayment))
    
    
