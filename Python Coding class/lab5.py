# Lab Number: 16A

# Name and Student Number: Joshua Noronha, 101194076

# Functions below this line:

def min_RRIF_withdrawal ( start_RRIF_balance: float, age: int)->float:
   """Returns the minimum withdrawal between the ages 55 to 70 using the parameters of age and start_RRIF_balance
   >>> min_RRIF_withdrawal(0.00, 55)
   0.0
   >>> min_RRIF_withdrawal(90.50, 70)
   4.525
   >>> min_RRIF_withdrawal(1000.50, 67)
   43.5
   >>> min_RRIF_withdrawal(0.00001, 62)
   0.0000003571428
   """
   X = (90-age)
   return start_RRIF_balance/X

def accrued_amount (Principal_Amount: float, rate: float, compounding_periods: float, time_in_years: float)->float:
   """Returns the compounded intrest using the parameters Principal_Amount, rate, compounding_periods, time_in_years
   >>> accrued_amount(0.0, 50, 365, 5) 
   0.0
   >>> accrued_amount(1000.0, 50, 52, 6.5) 
   25393.02
   >>>accrued_amount(999.89, 58.32, 2, 7.2) 
   39828.68
   """
   return Principal_Amount*(1+((rate/100)/compounding_periods))**(compounding_periods*time_in_years)
   
# Main Script below this line:

# Exercise 1
print ("\n Exercise 1 Outputs: \n") 

help(min_RRIF_withdrawal)

account_holder1= min_RRIF_withdrawal(0.00, 55)
print(format(account_holder1,".2f"))

account_holder2= min_RRIF_withdrawal(90.50, 70)
print(format(account_holder2,".2f"))

account_holder3= min_RRIF_withdrawal(1000.50, 67)
print(format(account_holder3,".2f"))

account_holder4= min_RRIF_withdrawal(0.00001, 62)
print(format(account_holder4,".2f"))

# Exercise 2
print ("\n Exercise 2 Outputs: \n") 

help(accrued_amount)

Calculation1= accrued_amount(0.0, 50.0, 365, 5.0) 
print (format(Calculation1,".2f")) 

Calculation2= accrued_amount(1000.0, 50, 52, 6.5) 
print (format(Calculation2,".2f")) 

Calculation3= accrued_amount(999.89, 58.32, 2, 7.2) 
print (format(Calculation3,".2f")) 

# No code below this line
print("\nEnd of file reached successfully")