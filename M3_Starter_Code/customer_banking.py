# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    savings_balance = 0
    cd_balance = 0
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("How much money do you currently have in your savings account: $ "))
    
    # Prompt user to input interest
    savings_interest_rate = int(input("What interest rate would you like? (in percentage)"))


    # Prompt user to input months
    savings_months = int(input("How many months have you had this account?"))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)


    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Savings Account:")
    print(f" - Initial Balance: ${savings_balance:.2f}")
    print(f" - Interest Earned: ${interest_earned:.2f}")
    print(f" - Updated Balance: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("How much money do you currently have in your CD account: $ "))

    # Prompt user to input interest
    cd_interest_rate = int(input("What interest rate would you like? (in percentage)"))

    # Prompt user to input months
    cd_months = int(input("How many months have you had this account?"))


    

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"CD ACCOUNT: ")
    print(f'-YOUR INTITAL BALANCE: ${cd_balance:.2f}')
    print(f"-INTEREST EARNED: ${interest_earned:.2f}")
    print(f"-Your new balance is: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function
    main()