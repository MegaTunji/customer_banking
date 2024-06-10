"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    
 # Create an instance of the `Account` class and pass in the balance and interest parameters.
    my_savings_account = Account("my savings acount", balance, interest_rate)
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    months = input(" How many months have you had this account? ")
    if months.isdigit():
        print(f"So to clarify is has been: {months} months?")

    else:
        print("The amount you enter is incorrect.")
    
    interest_rate = balance * (apr/100 * months/12)

      # Calculate interest earned
     # ADD YOUR CODE HERE
    interest_earned = interest_rate * months + balance
    print(f'The interested earned is : {interest_earned}')

     # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
def updated_save_balance( balance, interest_earned):
    updated_bal = balance + interest_earned

    return updated_bal

    
    

    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
  


    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
