import math
def cashier():
    """
    Simulates a cashier: asks the user for the amount to withdraw,
    checks if there is enough money in the account, and then subtracts
    the withdrawn amount from the balance.

    The initial balance is 83000.32
    """
    
    balance = float(83000.32)
    withdraw = float(input('Enter the amount to withdraw: '))
    if withdraw > balance:
        return print('You do not have enough money in your account')
    else:
        balance -= withdraw
        return print(f'Your balance is: {balance}')

cashier()