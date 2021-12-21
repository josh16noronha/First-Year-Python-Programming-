# Lab Number: 16A

# Name and Student Number: Joshua Noronha, 101194076

# Functions below this line:

def factorial(n: int) -> int:
 """
 Return n! for positive values of n
 and has to be non-negative
 
 >>> factorial(1)
 1
 >>> factorial(2)
 2
 >>> factorial(3)
 6
 >>> factorial(4)
 24
 """
 fact = 1
 for i in range(2,n+1):
  fact = fact * n

 return fact 

def tip(cost_of_meal: float, satisfaction: int)-> float:
 """
 Returns the amount of tip to give which is based on the cost_of_meal which is a postive value and the satisfaction of the customer which is on a scale of one to three where one is Totally satisfied
 satisfaction one is 20 percent
 satisfaction two is 15 percent
 satisfaction three is 5 percent
 
 >>>tip(0,1)
 0.0
 >>>tip(1000,3)
 50.0
 >>>tip(50.95,1)
 10.190000000000001
 """
 if satisfaction == 1: 
  option=(cost_of_meal*(20/100))
 elif satisfaction == 2: 
  option=(cost_of_meal*(15/100))
 elif satisfaction == 3: 
  option=(cost_of_meal*(5/100))
 else:
  print("Scale number does not exist") 
 return option 

def coupon(amount_spent_on_groceries: float)-> float:
 """
 Returns the value of the coupon in dollars using the parameter of amount_spent_on_groceries where no negative values are accepted only positive.
 No negative numbers
 
 >>>coupon(25.86)
 $ 2.0688
 >>>coupon(120)
 $ 12.0
 >>>coupon(0)
 $ No coupon
 >>>coupon(1000)
 $ 140.0
 >>>coupon(60.00)
 $ 4.8
 >>>coupon(50)
 $ 4.0
 """
 if amount_spent_on_groceries < 10:
  dollar_discount= (0.0)
 if 10 <= amount_spent_on_groceries <= 60:
  dollar_discount= (8/100)*amount_spent_on_groceries 
 if 60 < amount_spent_on_groceries <= 150:
  dollar_discount= (10/100)*amount_spent_on_groceries 
 if 150 < amount_spent_on_groceries <= 210:
  dollar_discount= (12/100)*amount_spent_on_groceries 
 if amount_spent_on_groceries > 210:
  dollar_discount= (14/100)*amount_spent_on_groceries  
 return dollar_discount

def test_int(discription: str, expected: int, actual: int)-> int:
 """
 Returns either 0 for test failed or 1 for test passed using the parameters of discription, expected, actual
 
 >>>test_int("factorial(1)", 1,factorial(1))
 Testing factorial(1)
Expected result: 1 Actual result: 1
Test passed
 
 >>>test_int("factorial(2)", 2,factorial(2))
 Testing factorial(2)
Expected result: 2 Actual result: 2
Test passed
 
 >>>test_int("factorial(3)", 6,factorial(3))
 Testing factorial(3)
Expected result: 6 Actual result: 9
Test failed
 
 >>>test_int("factorial(4)", 24,factorial(4))
 Testing factorial(4)
Expected result: 24 Actual result: 64
Test failed
 """

 print("Testing", discription)
 print("Expected result:", expected, "Actual result:", actual)
 if actual == expected:
  print("Test passed")
  return 1 
 else:
  print("Test failed")
  return 0

# Main Script below this line:

# Exercise 1
print ("\n Exercise 1 Outputs: \n") 

pass_counter = 0
total_test = 0

actual1 = factorial( 1 )
print( "Testing factorial(1) ")
print( "Expected result: 1, Actual result:", actual1)
total_test += 1
if actual1 == 1:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual2 = factorial( 2 )
print( "Testing factorial(2) ")
print( "Expected result: 2, Actual result:", actual2)
total_test += 1
if actual2 == 2 :
 print ("Test passed")
 pass_counter += 1
else:
  print ("Test failed")

actual3 = factorial( 3 )
print( "Testing factorial(3) ")
print( "Expected result: 6, Actual result:", actual3)
total_test += 1
if actual3 == 6 :
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual4 = factorial( 4 )
print( "Testing factorial(4) ")
print( "Expected result: 24, Actual result:", actual4)
total_test += 1
if actual4 == 24 :
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
print (pass_counter, "Tests passed for Exercise 1")
print (total_test-pass_counter,"Tests failed for Exercise 1")

# Exercise 2
print ("\n Exercise 2 Outputs: \n") 

pass_counter = 0
total_test = 0

meal_option= tip(0,1)
print(meal_option)  
meal_option= tip(1000,3)
print(meal_option) 
meal_option= tip(50.95,1)
print(meal_option) 
 
print("\n")
actual1 = tip(0,1)
print( "Testing tip(0,1) ")
print( "Expected result: 0.0, Actual result:", actual1)
total_test += 1
if actual1 == 0.0 :
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual2 = tip(1000,3)
print( "Testing tip(1000,3) ")
print( "Expected result: 50.0, Actual result:", actual2)
total_test += 1
if actual2 == 50.0 :
 print ("Test passed")
 pass_counter += 1
else:
  print ("Test failed")

actual3 = tip(50.95,1)
print( "Testing tip(50.95,1) ")
print( "Expected result: 10.190000000000001, Actual result:", actual3)
total_test += 1
if actual3 == 10.190000000000001:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
print (pass_counter, "Tests passed for Exercise 2")
print (total_test-pass_counter,"Tests failed for Exercise 2")


# Exercise 3
print ("\n Exercise 3 Outputs: \n") 

pass_counter = 0
total_test = 0

 
amount= coupon(25.86)
print("$",amount)
amount= coupon(120)
print("$",amount)
amount= coupon(0)
print("$",amount)
amount= coupon(1000)
print("$",amount)
amount= coupon(60.00)
print("$",amount)
amount= coupon(50)
print("$",amount)

print("\n")
actual1 = coupon(25.86)
print( "Testing coupon(25.86) ")
print( "Expected result: $ 2.0688, Actual result:", actual1)
total_test += 1
if actual1 == 2.0688:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual2 = coupon(120)
print( "Testing coupon(120) ")
print( "Expected result: $ 12.0, Actual result:", actual2)
total_test += 1
if actual2 == 12.0:
 print ("Test passed")
 pass_counter += 1
else:
  print ("Test failed")

actual3 = coupon(0)
print( "Testing coupon(0) ")
print( "Expected result: $ 0, Actual result:", actual3)
total_test += 1
if actual3 == 0:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual4 = coupon(1000)
print( "Testing coupon(1000) ")
print( "Expected result: $ 140.0, Actual result:", actual4)
total_test += 1
if abs(actual4-140.0) < 0.001:
 print ("Test passed")
 pass_counter += 1
else:
  print ("Test failed")

actual5 = coupon(60.00)
print( "Testing coupon(60.00) ")
print( "Expected result: $ 4.8, Actual result:", actual5)
total_test += 1
if abs(actual5 - 4.8) < 0.001:
  print ("Test passed")
  pass_counter += 1
else:
  print ("Test failed")

actual6 = coupon(50)
print( "Testing coupon(50) ")
print( "Expected result: $ 4.0, Actual result:", actual6)
total_test += 1
if abs(actual6 - 4.0) < 0.001:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
    
print (pass_counter, "Tests passed for Exercise 3")
print (total_test-pass_counter,"Tests failed for Exercise 3")

# Final Exercise 
print ("\n Final Exercise Outputs: \n") 

pass_counter = 0
total_test = 0

pass_counter += test_int("factorial(1)", 1,factorial(1))
total_test += 1
pass_counter += test_int("factorial(2)", 2,factorial(2))
total_test += 1
pass_counter += test_int("factorial(3)", 6,factorial(3))
total_test += 1
pass_counter += test_int("factorial(4)", 24,factorial(4))
total_test += 1

print (pass_counter, "Tests passed for Final Exercise")
print (total_test-pass_counter,"Tests failed for Final Exercise")


# No code below this line
print("\nEnd of file reached successfully")