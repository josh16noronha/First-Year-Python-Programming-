# Lab Number: 16A

# Name and Student Number: Joshua Noronha, 101194076

# Functions below this line:

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


def  bakers_party(num_pastries: int, weekend: bool)-> bool:
 """
 Returns if the party of the bakers is succesfull using the parameters of num_pastries and weekend
 but the restriction is that during the week for the party to be succesful between  40 and 60 
 pastries must be eaten no more no less, but on the weekend they can eat more than 40 for a 
 succesful party
 
 >>>bakers_party(100,True)
 True
 >>>bakers_party(10,False)
 False
 >>>bakers_party(47,False)
 True
 """
 FORTY=40
 SIXTY=60
 return (weekend == True) and (FORTY<=num_pastries) or ((weekend == False) and (FORTY<=num_pastries<=SIXTY))


def squirrel_play(temp: int, summer_season: bool)-> bool:
 """
 Returns if the squirrels in Palo Alto outside this is determined using the parameters temp which is in degrees fahrenheit (F) and summer_season
 If the temperature is between 60 and 90 and the season is not summer then they are playing outside, but if it is the summer season and the temperature
 is 60 and 100 then they will be playing outside
 
 >>>squirrel_play(70,False)
 True
 >>>squirrel_play(97, True)
  True
 >>>squirrel_play(91,False)
 False
 """
 SIXTY=60
 HUNDRED=100
 NINTY=90
 return (SIXTY<=temp<=HUNDRED) and (summer_season== True) or ((SIXTY<=temp<=NINTY) and (summer_season== False))

def great_42(a: int, b: int)-> bool:
 """
 Returns if a or b is equal to 42, or if the addition of a and b will equal to 42, or if the subtraction of a and b will equal to 42
 If the value is -42 it is still 42 so the output should be True
 
 >>>great_42(-12,-42)
 True
 >>>great_42(22,20)
 True
 >>>great_42(0,42)
 True
 >>>great_42(0,0)
 False
 """
 FORTY_TWO=42
 return (abs(a)== FORTY_TWO or abs(b)== FORTY_TWO) or ((abs(a+b)== FORTY_TWO or abs(b+a)== FORTY_TWO)) or ((abs(a-b)== FORTY_TWO or abs(b-a)== FORTY_TWO))
 
def blackjack(a: int, b: int)-> int:
 """ 
 Returns a value which is closest to 21 without going over 21 using the parameters of a and b
 
 >>>blackjack(19,20)
 20
 >>>blackjack(19,21)
 21
 >>>blackjack(17,22)
 17
 """
 TWENTY_ONE=21
 ZERO=0
 if (a>TWENTY_ONE):
  return b
 if (b>TWENTY_ONE):
  return a
 if ((a<=TWENTY_ONE) and not(a>TWENTY_ONE) and (a>b)):
   return a
 if ((b<=TWENTY_ONE) and not(b>TWENTY_ONE) and (b>a)):  
  return b
 else:
  return ZERO
 
def sum_uniques(a: int, b: int, c: int)->int:
 """
 Returns the sum of three prarmeters a, b, c 
 but if any of the values within the parameters are the same then it will be not used when finding the sum

 >>>sum_uniques(3,2,3)
 2
 >>>sum_uniques(3,3,3)
 0
 >>>sum_uniques(4,5,20)
 29
 """
 ZERO=0
 if (a==b==c):
  return ZERO
 if (a==b):
  return c
 if (b==c):
  return a
 if (c==a):
  return b
 else:
  return a+b+c
 
# Main Script below this line:

# Exercise 1
print ("\n Exercise 1 Outputs: \n") 

pass_counter = 0
total_test = 0

event=bakers_party(100,True)
print(event)
event=bakers_party(10,False)
print(event)
event=bakers_party(47,False)
print(event)

print("\n")
actual1 = bakers_party(100,True)
print( "Testing bakers_party(100,True) ")
print( "Expected result: True, Actual result:", actual1)
total_test += 1
if actual1 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual2 = bakers_party(10,False)
print( "Testing bakers_party(10,False) ")
print( "Expected result: False, Actual result:", actual2)
total_test += 1
if actual2 == False:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual3 = bakers_party(47,False)
print( "Testing bakers_party(47,False) ")
print( "Expected result: True, Actual result:", actual3)
total_test += 1
if actual3 == True:
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

test=squirrel_play(70,False)
print(test)
test=squirrel_play(97, True)
print(test)
test=squirrel_play(91,False)
print(test)

print("\n")
actual1 = squirrel_play(70,False)
print( "Testing squirrel_play(70,False) ")
print( "Expected result: True, Actual result:", actual1)
total_test += 1
if actual1 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual2 = squirrel_play(97, True)
print( "Testing squirrel_play(97, True) ")
print( "Expected result: True, Actual result:", actual2)
total_test += 1
if actual2 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual3 = squirrel_play(91,False)
print( "Testing squirrel_play(91,False)")
print( "Expected result: False, Actual result:", actual3)
total_test += 1
if actual3 == False:
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

test=great_42(-12,-42)
print(test)
test=great_42(22,20)
print(test)
test=great_42(0,42)
print(test)
test=great_42(0,0)
print(test)

print("\n")
actual1 = great_42(-12,-42)
print( "Testing great_42(-12,-42) ")
print( "Expected result: True, Actual result:", actual1)
total_test += 1
if actual1 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual2 = great_42(22,20)
print( "Testing great_42(22,20) ")
print( "Expected result: True, Actual result:", actual2)
total_test += 1
if actual2 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual3 = great_42(0,42)
print( "Testing great_42(0,42) ")
print( "Expected result: True, Actual result:", actual3)
total_test += 1
if actual3 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
actual4 = great_42(0,0)
print( "Testing great_42(0,0) ")
print( "Expected result: False, Actual result:", actual4)
total_test += 1
if actual4 == False:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")  
 
 
print (pass_counter, "Tests passed for Exercise 3")
print (total_test-pass_counter,"Tests failed for Exercise 3") 

# Exercise 4
print ("\n Exercise 4 Outputs: \n")

pass_counter = 0
total_test = 0

test=blackjack(19,20)
print(test)
test=blackjack(19,21)
print(test)
test=blackjack(17,22)
print(test)

print("\n")
actual1 = blackjack(19,20)
print( "Testing blackjack(19,20) ")
print( "Expected result: 20, Actual result:", actual1)
total_test += 1
if actual1 == 20:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual2 = blackjack(19,21)
print( "Testing blackjack(19,21) ")
print( "Expected result: 21, Actual result:", actual2)
total_test += 1
if actual2 == 21:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
actual3 = blackjack(17,22)
print( "Testing blackjack(17,22) ")
print( "Expected result: 17, Actual result:", actual3)
total_test += 1
if actual3 == 17:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")  
 
print (pass_counter, "Tests passed for Exercise 4")
print (total_test-pass_counter,"Tests failed for Exercise 4")  

# Exercise 5
print ("\n Exercise 5 Outputs: \n")

pass_counter = 0
total_test = 0

test=sum_uniques(3,2,3)
print(test)
test=sum_uniques(3,3,3)
print(test)
test=sum_uniques(4,5,20)
print(test)

print("\n")
actual1 = sum_uniques(3,2,3)
print( "Testing sum_uniques(3,2,3) ")
print( "Expected result: 2, Actual result:", actual1)
total_test += 1
if actual1 == 2:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual2 = sum_uniques(3,3,3)
print( "Testing sum_uniques(3,3,3) ")
print( "Expected result: 0, Actual result:", actual2)
total_test += 1
if actual2 == 0:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 

actual3 = sum_uniques(4,5,20)
print( "Testing sum_uniques(4,5,20) ")
print( "Expected result: 29, Actual result:", actual3)
total_test += 1
if actual3 == 29:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
print (pass_counter, "Tests passed for Exercise 5")
print (total_test-pass_counter,"Tests failed for Exercise 5")  

# Final Exercise 
print ("\n Final Exercise Outputs: \n")

print("I have made the two improvements to all the exercises, I changed the hard-coded values into CONSTANTS and simplified and shortned code that followed the requirements needed on the rubric")


# No code below this line
print("\nEnd of file reached successfully")