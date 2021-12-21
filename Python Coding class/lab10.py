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

def count_evens(lst: list)-> int:
    """
    Returns all even numbers in the list using the parameter of lst
    Assumption is that any negative number that is divisible by 2 is even
    and 0 is an even number.
    If list empty then return "nothing in list"
    
    >>>count_evens(lst)
    5
    >>>count_evens(lst1)
    nothing in list
    >>>count_evens(lst2)
    3
    """
    counter=0
    even=0
    if not lst:
        return ("nothing in list")
    while counter < len(lst):
        if lst[counter]%2 == 0:   
            even+=1
        counter += 1
    return (even) 
   
def big_diff(lst: list)->int:
 """
 Returns the difference of the largest and smallest values in the list using the parameter of lst
 An assumption is that there is at least two integers in the list
 
 >>>big_diff(lst)
 350
 >>>big_diff(lst1)
 12
 >>>big_diff(lst2)
 55
 """
 biggest_value = lst[0]
 for i in lst:
     if biggest_value < i:
         biggest_value = i

 smallest_value = lst[0]
 for i in lst:
     if smallest_value > i:
         smallest_value = i
         
 return (biggest_value - smallest_value)
 
def has22(lst: list)->bool:
 """
 Returns True if there is a 2 next to another 2 in the list, and returns False for any other cercomestances. The parameter for this function is lst.
 The assumption that can be made is that if the list is empty then the function will return a False.

>>>has22(lst)
False
>>>has22(lst1)
True
>>>has22(lst2)
False
"""
 for i in range(0, len(lst)-1):
  if lst[i] == 2 and lst[i+1]==2:
   return True
 return False

def centered_average(lst: list)->int:
 """
 Returns the centered average of the list that is put into the parameter of lst.
 An assumption is that the list has to have at least three integers and list cannot be empty.
 
 >>>centered_average(lst)
 5.2
 >>>centered_average(lst1)
 35.0
 >>>centered_average(lst2)
 39.5
 """
 adding=0
 for i in lst:
  adding+=i
  lenth_list= (len(lst)-2)
 return(adding-max(lst)-min(lst)) / lenth_list

def sum13(lst: list)->int:
 """
 Returns the sum of the list, but returns 0 if the list is empty, lastly if the list 
 contains the number 13 then 13 and the next number is avoided. The parameter is lst.

>>>sum13(lst) 
3
>>>sum13(lst1) 
6
>>>sum13(lst2) 
0
 """
 sum_of_list=0
 i=0
 while  i < len(lst):
     if lst[ i] != 13:
         sum_of_list += lst[i]
     else:
         i += 1 
     i += 1

 return sum_of_list

def sum67(lst: list)->int:
 """
 Returns the sum of the list which avoids any numbers in the list from six to seven.
 The parameter is lst. An assumption is that there can be any values in the list that are integers.
 
 >>>sum67(lst)
 5
 >>>sum67(lst1)
 0
 >>>sum67(lst2)
 945
 """
 if not lst:
     return 0
 sum_of_list=0
 indicator= True
 for i in range(len(lst)):
     if lst[i]==6:
         indicator=False
     elif lst[i]==7 and indicator==False:
         indicator=True
     elif indicator==True:
         sum_of_list += lst[i]
 return sum_of_list

def bank_statement(lst: list)->list:
 """
 Returns a list of three values the first is the total deposit, the next value will be the total withdrawals, and lastly in the list is the current acount ballance.
 The parameter is lst which is a list. 
 An assumption is that the list cannot be empty.
 
 >>>bank_statement(lst) 
 [28.74, -11.57, 17.17]
 >>>bank_statement(lst1) 
 [75, -240, -165]
 >>>bank_statement(lst2) 
 [538, -5, 533]
 """
 sum_of_withdrawals=0
 sum_of_deposits=0
 for i in range(len(lst)):
     if lst[i]>0:
         sum_of_deposits += lst[i]
     if lst[i]<0:
          sum_of_withdrawals += lst[i]
     bank_account= (sum_of_deposits)+(sum_of_withdrawals)      
 return [ round(sum_of_deposits,2), round(sum_of_withdrawals,2),round(bank_account,2)]

def divisors(n: int)->list:
 """
 Returns a list containing all positive divisors of n. The parameter is n and the assumption is that n should not be empty
 
 >>>divisors(6)
 [1, 2, 3, 6]
 >>>divisors(20)
 [1, 2, 4, 5, 10, 20]
 >>>divisors(89)
 [1, 89]
 """
 new_list=[]
 for i in range(1,n+1):
  if n%i==0:
    new_list += [i]
 return new_list
             
def reverse(lst: int)->list:
 """
 Returns the reverse of the list in the parameter, using the parameter of lst.
 Assumption is that if the list is empty then print empty list as so [] 
 
 >>> reverse([4, 2, 3, 2])
 [2, 3, 2, 4]
 >>>reverse([])
 []
 >>>reverse([5,5,24,1,6,8,7,20,4,5,3,12,5,8,9,20])
 [20, 9, 8, 5, 12, 3, 5, 4, 20, 7, 8, 6, 1, 24, 5, 5]
 """
 new_list=[0]*len(lst)
 
 for i in range(len(lst)):
  new_list[i]= lst[len(lst)-i-1]
 return new_list
  
 
# Main Script below this line:

# Exercise 1
print ("\n Exercise 1 Outputs: \n") 

pass_counter = 0
total_test = 0

lst=[1,0,4,5,-4,-9,10,100]
test_function = count_evens(lst)
print(test_function)

lst1=[]
test_function = count_evens(lst1)
print(test_function)

lst2=[-50,65,1,47,52,30]
test_function = count_evens(lst2)
print(test_function)

print("\n")
actual = count_evens(lst)
print( "Testing count_evens(lst) ")
print( "Expected result: 5, Actual result:", actual)
total_test += 1
if actual == 5:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual1 = count_evens(lst1)
print( "Testing count_evens(lst1) ")
print( "Expected result: 'nothing in list', Actual result:", actual1)
total_test += 1
if actual1 == 'nothing in list':
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual2 = count_evens(lst2)
print( "Testing count_evens(lst2) ")
print( "Expected result: 3, Actual result:", actual2)
total_test += 1
if actual2 == 3:
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

lst=[-50,65,100,0,52,300]
test_function = big_diff(lst)
print(test_function)

lst1=[10,22,20]
test_function = big_diff(lst1)
print(test_function)

lst2=[10,22,20,55,8,0]
test_function = big_diff(lst2)
print(test_function)

print("\n")
actual = big_diff(lst)
print( "Testing big_diff(lst) ")
print( "Expected result: 350, Actual result:", actual)
total_test += 1
if actual == 350:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual = big_diff(lst1)
print( "Testing big_diff(lst1) ")
print( "Expected result: 12, Actual result:", actual)
total_test += 1
if actual == 12:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
actual = big_diff(lst2)
print( "Testing big_diff(lst2) ")
print( "Expected result: 55, Actual result:", actual)
total_test += 1
if actual == 55:
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

lst=[]
test_function = has22(lst)
print(test_function)

lst1=[0,27,1,4,5,6,2,0,10,60,2,2,251]
test_function = has22(lst1)
print(test_function)

lst2=[10,53,2,0,2]
test_function = has22(lst2)
print(test_function)

print("\n")
actual = has22(lst)
print( "Testing has22(lst) ")
print( "Expected result: False, Actual result:", actual)
total_test += 1
if actual == False:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual = has22(lst1)
print( "Testing has22(lst1) ")
print( "Expected result: True, Actual result:", actual)
total_test += 1
if actual == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
actual = has22(lst2)
print( "Testing has22(lst2) ")
print( "Expected result: False, Actual result:", actual)
total_test += 1
if actual == False:
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

lst=  [1, 1, 5, 5, 10, 8, 7]
test_function = centered_average(lst)
print(test_function)

lst1=  [25,900,35]
test_function = centered_average(lst1)
print(test_function)

lst2=  [85,93,-50,-6]
test_function = centered_average(lst2)
print(test_function)

print("\n")
actual = centered_average(lst)
print( "Testing centered_average(lst) ")
print( "Expected result: 5.2, Actual result:", actual)
total_test += 1
if actual == 5.2:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual = centered_average(lst1)
print( "Testing centered_average(lst1) ")
print( "Expected result: 35.0, Actual result:", actual)
total_test += 1
if actual == 35.0:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
actual = centered_average(lst2)
print( "Testing centered_average(lst2) ")
print( "Expected result: 39.5, Actual result:", actual)
total_test += 1
if actual == 39.5:
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

lst= [13, 1, 2, 13,2, 1, 13]
test_function = sum13(lst)
print(test_function)

lst1= [1, 2, 2, 1, 13]
test_function = sum13(lst1)
print(test_function)

lst2= []
test_function = sum13(lst2)
print(test_function)

print("\n")
actual = sum13(lst)
print( "Testing sum13(lst) ")
print( "Expected result: 3, Actual result:", actual)
total_test += 1
if actual == 3:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual = sum13(lst1)
print( "Testing sum13(lst1) ")
print( "Expected result: 6, Actual result:", actual)
total_test += 1
if actual == 6:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
actual = sum13(lst2)
print( "Testing sum13(lst2) ")
print( "Expected result: 0, Actual result:", actual)
total_test += 1
if actual == 0:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")  
 
print (pass_counter, "Tests passed for Exercise 5")
print (total_test-pass_counter,"Tests failed for Exercise 5")   

# Exercise 6
print ("\n Exercise 6 Outputs: \n") 

pass_counter = 0
total_test = 0

lst= [1, 2, 2, 6, 99, 99, 7]
test_function = sum67(lst)
print(test_function)

lst1= []
test_function = sum67(lst1)
print(test_function)

lst2= [6,5,500,4,8,9,5,3,2,1,7,945,6,2,4,0,8,7]
test_function = sum67(lst2)
print(test_function)

print("\n")
actual = sum67(lst)
print( "Testing sum67(lst) ")
print( "Expected result: 5, Actual result:", actual)
total_test += 1
if actual == 5:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual = sum67(lst1)
print( "Testing sum67(lst1) ")
print( "Expected result: 0, Actual result:", actual)
total_test += 1
if actual == 0:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual = sum67(lst2)
print( "Testing sum67(lst2) ")
print( "Expected result: 945, Actual result:", actual)
total_test += 1
if actual == 945:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

print (pass_counter, "Tests passed for Exercise 6")
print (total_test-pass_counter,"Tests failed for Exercise 6") 

# Exercise 7
print ("\n Exercise 7 Outputs: \n") 

pass_counter = 0
total_test = 0

lst= [1.25, -1.569840, 5.98, 6.51, -10, 8, 7]
test_function = bank_statement(lst)
print(test_function)

lst1= [25,-5,5,-90,-61,-5,-32,-47,45]
test_function = bank_statement(lst1)
print(test_function)

lst2= [0,56,482,-5]
test_function = bank_statement(lst2)
print(test_function)

print("\n")
actual = bank_statement(lst)
print( "Testing bank_statement(lst) ")
print( "Expected result: [28.74, -11.57, 17.17], Actual result:", actual)
total_test += 1
if actual == [28.74, -11.57, 17.17]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual = bank_statement(lst1)
print( "Testing bank_statement(lst1) ")
print( "Expected result: [75, -240, -165], Actual result:", actual)
total_test += 1
if actual == [75, -240, -165]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
actual = bank_statement(lst2)
print( "Testing bank_statement(lst2) ")
print( "Expected result: [538, -5, 533], Actual result:", actual)
total_test += 1
if actual == [538, -5, 533]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
print (pass_counter, "Tests passed for Exercise 7")
print (total_test-pass_counter,"Tests failed for Exercise 7") 

# Exercise 8
print ("\n Exercise 8 Outputs: \n") 

pass_counter = 0
total_test = 0

n = 6
test_function = divisors(n)
print(test_function)

n1 = 20
test_function = divisors(n1)
print(test_function)

n2 = 89
test_function = divisors(n2)
print(test_function)

print("\n")
actual = divisors(n)
print( "Testing divisors(n) ")
print( "Expected result: [1, 2, 3, 6], Actual result:", actual)
total_test += 1
if actual == [1, 2, 3, 6]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual = divisors(n1)
print( "Testing divisors(n1) ")
print( "Expected result: [1, 2, 4, 5, 10, 20], Actual result:", actual)
total_test += 1
if actual == [1, 2, 4, 5, 10, 20]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual = divisors(n2)
print( "Testing divisors(n2) ")
print( "Expected result: [1, 89], Actual result:", actual)
total_test += 1
if actual == [1, 89]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
print (pass_counter, "Tests passed for Exercise 8")
print (total_test-pass_counter,"Tests failed for Exercise 8")  

# Exercise 9
print ("\n Exercise 9 Outputs: \n") 

pass_counter = 0
total_test = 0

lst= [4, 2, 3, 2]
test_function = reverse(lst)
print(test_function)

lst1= []
test_function = reverse(lst1)
print(test_function)

lst2= [5,5,24,1,6,8,7,20,4,5,3,12,5,8,9,20]
test_function = reverse(lst2)
print(test_function)

print("\n")
actual = reverse(lst)
print( "Testing reverse(lst) ")
print( "Expected result:[2, 3, 2, 4], Actual result:", actual)
total_test += 1
if actual == [2, 3, 2, 4]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual = reverse(lst1)
print( "Testing reverse(lst1) ")
print( "Expected result:[], Actual result:", actual)
total_test += 1
if actual == []:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
actual = reverse(lst2)
print( "Testing reverse(lst2) ")
print( "Expected result:[20, 9, 8, 5, 12, 3, 5, 4, 20, 7, 8, 6, 1, 24, 5, 5], Actual result:", actual)
total_test += 1
if actual == [20, 9, 8, 5, 12, 3, 5, 4, 20, 7, 8, 6, 1, 24, 5, 5]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 

print (pass_counter, "Tests passed for Exercise 9")
print (total_test-pass_counter,"Tests failed for Exercise 9")   