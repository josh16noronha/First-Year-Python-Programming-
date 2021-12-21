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


def first_last6 (lst: list, target: int)->bool:
    """
    Returns Ture if a 6 is either first or last or both in the list, or else it will return False, the parameters that I am using are lst and target. The assumption that is being made is that the list cannot be empty.
    
    >>>first_last6(list1,6)
    True
    >>>first_last6(list2,6)
    True
    >>>first_last6(list3,6)
    True
    >>>first_last6(list4,6)
    False
    >>>first_last6(list5,6)
    False
    """
    if (lst[0] == 6) and (lst[len(lst)-1] == 6):
        return True
    elif (lst[0] == 6) or (lst[len(lst)-1] == 6):
        return True
    return False

def same_first_last(lst: list)->bool:
 """
 Returns True if the first and last elements in the list is equal to eachother and if the list is not empty, else it will return False. The assumptions that I can make are that the list can be empty in this.
 
 >>>same_first_last(lst1)
 False
 >>>same_first_last(lst2)
 True
 >>>same_first_last(lst3)
 True
 >>>same_first_last(lst4)
 False
 """
 if not lst:
  return False
 elif (lst[len(lst)-1] == lst[0]):
  return True
 return False

import math

def make_pi()->list:
 """
 Returns a list of 3 boxes which are the first three digits of pi
 
 >>>make_pi()
 [3, 1, 4] 
 """
 return [3,1,4] 

def common_end(lst: list, lst1: list)->bool:
 """
 Returns True if both lists contain the same first element or last element or both, 
 else it will return False, the parameters are lst, and lst1
 An assumption is that every value in the list is an integer 
 
 >>>common_end(lst,lst1)
 True
 >>>common_end(lst2,lst3)
 True
 >>>common_end(lst4,lst5)
 True
 >>>common_end(lst6,lst7)
 False
 """
 if (lst[0]==lst1[0]) or (lst[-1]==lst1[-1]) or (lst[0]==lst1[0] and lst[-1]==lst1[-1]):
  return True
 return False

def sum3(lst: list)->int:
 """
 Returns the sum of the 3 integer values in stored in the list in the parameter of lst
 Assumption is that the list always has to have 3 values in the list no more no less
 
 >>>sum3(lst)
 6
 >>>sum3(lst1)
 96
 >>>sum3(lst2)
 47
 """
 if True:
  return int (lst[0]+lst[1]+lst[2])

def rotate_left3(lst: list)->list:
 """
 Returns the same elements where the position is moved to the left, using the parameter of lst
 An assumtion that is made is that there cannot be less or more than three elements  
 
 >>>rotate_left3(lst4)
 [2, 3, 1]
 >>>rotate_left3(lst3)
 [53, 1000, -92]
 >>>rotate_left3(lst5)
 [43, 25, 10]
 """
 first= lst[1]
 second= lst[2]
 third= lst[0]
 return [first,second,third]

def reverse3(lst: list)->list:
 """
 Returns a list that is in the opposite order than what is present in the list, using the parameter of lst
An assumtion that is made is that there cannot be less or more than three elements 
 >>>reverse3(lst1)
 [3, 2, 1]
 >>>reverse3(lst2)
 [-3, -62, 58]
 >>>reverse3(lst3)
 [-4, 0, 87]
  """
 first= lst[2]
 second= lst[1]
 third= lst[0]
 return [first,second,third]

def max_end3(lst: list)->list:
 """
 Returns a list of three values of the highest value found in the list in the parameter lst
 An assumtion that is made is that there cannot be less or more than three elements 
 
 >>>max_end3(lst1)
 [3, 3, 3]
 >>>max_end3(lst2)
 [200, 200, 200]
 >>>max_end3(lst3)
 [50, 50, 50]
 """
 first= lst[0]
 last= lst[2] 
 if first < last:
  return [last,last,last]
 return [first,first,first]

def sum2(lst:list)->int:
 """
 Returns the sum of the first and second integers in the list in the parameter of sum2, or returns 0 if the list is empty or it has only one element.
 An assumption is that the list has no constraints on its length
 
 >>>sum2(lst)
 0
 >>>sum2(lst1)
 0
 >>>sum2(lst2)
 5
 """
 if len(lst)==0 or len(lst)==1:
  return 0
 return lst[0]+lst[1]

def middle_way(lst: list, lst1: list)->list:
 """
 Returns a new list that contains the middle value of both lists in the parameters of lst and lst1 
  An assumtion that is made is that there cannot be less or more than three elements in each list and the lists cannot be empty
  
  >>>middle_way(lst2,lst3)
  [2, 5]
  >>>middle_way(lst4,lst5)
  [-60, 28]
  >>>middle_way(lst6,lst7)
  [1000, -1000]
 """
 middle_lst= lst[1]
 middle_lst1= lst1[1]
 new_lst=[middle_lst,middle_lst1]
 return new_lst

def make_ends(lst: list)->list:
 """
 Returns a new list comprised of the first and last elements of the list using the parameter of lst
 An Assumption is that the lst is not empty 
 
 >>>make_ends(lst)
 [4,7]
 >>>make_ends(lst1)
 [10, 7]
 >>>make_ends(lst2)
 [8, 8]
 """
 lst_first= lst[0]
 lst_last= lst[len(lst)-1]
 new_lst= [lst_first,lst_last]
 return new_lst

def has23(lst: list)->bool:
 """
 Returns True if the list contains either 2 or 3 or both in the list, it will return False if that condition is not met. The parameter of the function is lst
 An assumption is that the list will have 2 integers
 
 >>>has23(lst)
 False
 >>>has23(lst1)
 True
 >>>has23(lst2)
 True
 """
 if (lst[0]==2 or lst[0]==3) or (lst[1]==2 or lst[1]==3):
  return True
 return False
 
# Main Script below this line:

# Exercise 1
print ("\n Exercise 1 Outputs: \n") 

pass_counter = 0
total_test = 0

list1=[6,1,2,3,0]
test_function= first_last6(list1,6)
print(test_function)

list2=[7,-58,9,47,-5,1,2,38,6]
test_function= first_last6(list2,6)
print(test_function)

list3=[6,48,6]
test_function= first_last6(list3,6)
print(test_function)

list4=[68,-42,0,23,-48,10]
test_function= first_last6(list4,6)
print(test_function)

list5=[3,6,6,6,6,6,6,6,-6,6,6,6,6,6,6,6,6,6,-6,6,6,6,6,6,6,6,6,58]
test_function= first_last6(list5,6)
print(test_function)

print("\n")
actual1 = first_last6(list1,6)
print( "Testing first_last6(list1,6) ")
print( "Expected result: True, Actual result:", actual1)
total_test += 1
if actual1 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual2 = first_last6(list2,6)
print( "Testing first_last6(list2,6) ")
print( "Expected result: True, Actual result:", actual2)
total_test += 1
if actual2 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual3 = first_last6(list3,6)
print( "Testing first_last6(list3,6) ")
print( "Expected result: True, Actual result:", actual3)
total_test += 1
if actual3 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual4 = first_last6(list4,6)
print( "Testing first_last6(list4,6) ")
print( "Expected result: False, Actual result:", actual4)
total_test += 1
if actual4 == False:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual5 = first_last6(list5,6)
print( "Testing first_last6(list5,6) ")
print( "Expected result: False, Actual result:", actual5)
total_test += 1
if actual5 == False:
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

lst1 = [0,1,2,3,7]
test_function= same_first_last(lst1)
print(test_function)

lst2 = [0.00012,1,2,3,7,-54,82,0.00012]
test_function= same_first_last(lst2)
print(test_function)

lst3 = [0.00012,1,2,3,7,-54,82,0.00012]
test_function= same_first_last(lst3)
print(test_function)

lst4 = []
test_function= same_first_last(lst4)
print(test_function)

print("\n")
actual1 = same_first_last(lst1)
print( "Testing same_first_last(lst1) ")
print( "Expected result: False, Actual result:", actual1)
total_test += 1
if actual1 == False:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual2 = same_first_last(lst2)
print( "Testing same_first_last(lst2) ")
print( "Expected result: True, Actual result:", actual2)
total_test += 1
if actual2 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 

actual3 = same_first_last(lst3)
print( "Testing same_first_last(lst3) ")
print( "Expected result: True, Actual result:", actual3)
total_test += 1
if actual3 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
actual4 = same_first_last(lst4)
print( "Testing same_first_last(lst4) ")
print( "Expected result: False, Actual result:", actual4)
total_test += 1
if actual4 == False:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
print (pass_counter, "Tests passed for Exercise 2")
print (total_test-pass_counter,"Tests failed for Exercise 2")

# Exercise 3
print ("\n Exercise 3 Outputs: \n") 

print(make_pi())

# Exercise 4
print ("\n Exercise 4 Outputs: \n") 

pass_counter = 0
total_test = 0

lst=[0,1,2,3,4,5,6,7,8,9]
lst1=[0,56,85,90]
test_function = common_end(lst,lst1)
print(test_function)

lst2=[72,5,9,45,8]
lst3=[59,4,2,87,6,3,1,54,8,62,10,8]
test_function = common_end(lst2,lst3)
print(test_function)

lst4=[50,1,2,38,4,5,86,7,8,50]
lst5=[50,6,50]
test_function = common_end(lst4,lst5)
print(test_function)

lst6=[25,86,94,75,20]
lst7=[95,1000,58,73,54,99]
test_function = common_end(lst6,lst7)
print(test_function)

print("\n")
actual1 = common_end(lst,lst1)
print( "Testing common_end(lst,lst1) ")
print( "Expected result: True, Actual result:", actual1)
total_test += 1
if actual1 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual2 = common_end(lst2,lst3)
print( "Testing common_end(lst2,lst3) ")
print( "Expected result: True, Actual result:", actual2)
total_test += 1
if actual2 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
actual3 = common_end(lst4,lst5)
print( "Testing common_end(lst4,lst5) ")
print( "Expected result: True, Actual result:", actual3)
total_test += 1
if actual3 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")  
 
actual4 = common_end(lst6,lst7)
print( "Testing common_end(lst6,lst7) ")
print( "Expected result: False, Actual result:", actual4)
total_test += 1
if actual4 == False:
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

lst=[1,2,3]
test_function = sum3(lst)
print(test_function)

lst1=[0,4,92]
test_function = sum3(lst1)
print(test_function)

lst2=[71,-62,38]
test_function = sum3(lst2)
print(test_function)

print("\n")
actual1 = sum3(lst)
print( "Testing sum3(lst) ")
print( "Expected result: 6, Actual result:", actual1)
total_test += 1
if actual1 == 6:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual2 = sum3(lst1)
print( "Testing sum3(lst1) ")
print( "Expected result: 96, Actual result:", actual2)
total_test += 1
if actual2 == 96:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
actual3 = sum3(lst2)
print( "Testing sum3(lst2) ")
print( "Expected result: 47, Actual result:", actual3)
total_test += 1
if actual3 == 47:
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

lst3=[1,2,3]
test_function = rotate_left3(lst3)
print(test_function)

lst4=[-92,53,1000]
test_function = rotate_left3(lst4)
print(test_function)

lst5=[10,43,25]
test_function = rotate_left3(lst5)
print(test_function)

print("\n")
actual2 = rotate_left3(lst4)
print( "Testing rotate_left3(lst4) ")
print( "Expected result: [53, 1000, -92], Actual result:", actual2)
total_test += 1
if actual2 == [53, 1000, -92]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual1 = rotate_left3(lst3)
print( "Testing rotate_left3(lst3) ")
print( "Expected result: [2, 3, 1], Actual result:", actual1)
total_test += 1
if actual1 == [2, 3, 1]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
actual4 = rotate_left3(lst5)
print( "Testing rotate_left3(lst5) ")
print( "Expected result: 43, 25, 10], Actual result:", actual4)
total_test += 1
if actual4 == [43, 25, 10]:
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

lst1=[1,2,3]
test_function = reverse3(lst1)
print(test_function)

lst2=[58,-62,-3]
test_function = reverse3(lst2)
print(test_function)

lst3=[87,0,-4]
test_function = reverse3(lst3)
print(test_function)

print("\n")
actual1 = reverse3(lst1)
print( "Testing reverse3(lst1) ")
print( "Expected result: [3, 2, 1], Actual result:", actual1)
total_test += 1
if actual1 == [3, 2, 1]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual2 = reverse3(lst2)
print( "Testing reverse3(lst2) ")
print( "Expected result: [-3, -62, 58], Actual result:", actual2)
total_test += 1
if actual2 == [-3, -62, 58]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual3 = reverse3(lst3)
print( "Testing reverse3(lst3) ")
print( "Expected result: [-4, 0, 87], Actual result:", actual3)
total_test += 1
if actual3 == [-4, 0, 87]:
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

lst1=[1,2,3]
test_function = max_end3(lst1)
print(test_function)

lst2=[200,56,25]
test_function = max_end3(lst2)
print(test_function)

lst3=[50,56,50]
test_function = max_end3(lst3)
print(test_function)

print("\n")
actual1 = max_end3(lst1)
print( "Testing max_end3(lst1) ")
print( "Expected result: [3, 3, 3], Actual result:", actual1)
total_test += 1
if actual1 == [3, 3, 3]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual2 = max_end3(lst2)
print( "Testing max_end3(lst2) ")
print( "Expected result: [200, 200, 200], Actual result:", actual2)
total_test += 1
if actual2 == [200, 200, 200]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

actual3 = max_end3(lst3)
print( "Testing max_end3(lst3) ")
print( "Expected result: [50, 50, 50], Actual result:", actual3)
total_test += 1
if actual3 == [50, 50, 50]:
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

lst=[]
test_function = sum2(lst)
print(test_function)

lst1=[2]
test_function = sum2(lst1)
print(test_function)

lst2=[1,4,3]
test_function = sum2(lst2)
print(test_function)

print("\n")
actual1 = sum2(lst)
print( "Testing sum2(lst) ")
print( "Expected result: 0, Actual result:", actual1)
total_test += 1
if actual1 == 0:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual2 = sum2(lst1)
print( "Testing sum2(lst1) ")
print( "Expected result: 0, Actual result:", actual2)
total_test += 1
if actual2 == 0:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual3 = sum2(lst2)
print( "Testing sum2(lst2) ")
print( "Expected result: 5, Actual result:", actual3)
total_test += 1
if actual3 == 5:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
print (pass_counter, "Tests passed for Exercise 9")
print (total_test-pass_counter,"Tests failed for Exercise 9")    

# Exercise 10
print ("\n Exercise 10 Outputs: \n") 

pass_counter = 0
total_test = 0

lst2=[1,2,3]
lst3=[4,5,6]
test_function = middle_way(lst2,lst3)
print(test_function)

lst4=[45,-60,5]
lst5=[100,28,37]
test_function = middle_way(lst4,lst5)
print(test_function)

lst6=[5,1000,28]
lst7=[0,-1000,74]
test_function = middle_way(lst6,lst7)
print(test_function)

print("\n")
actual1 = middle_way(lst2,lst3)
print( "Testing middle_way(lst2,lst3) ")
print( "Expected result: [2, 5], Actual result:", actual1)
total_test += 1
if actual1 == [2, 5]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual2 = middle_way(lst4,lst5)
print( "Testing middle_way(lst4,lst5) ")
print( "Expected result: [-60, 28], Actual result:", actual2)
total_test += 1
if actual2 == [-60, 28]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual3 = middle_way(lst6,lst7)
print( "Testing middle_way(lst6,lst7) ")
print( "Expected result: [1000, -1000], Actual result:", actual3)
total_test += 1
if actual3 == [1000, -1000]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed") 
 
print (pass_counter, "Tests passed for Exercise 10")
print (total_test-pass_counter,"Tests failed for Exercise 10")    

# Exercise 11
print ("\n Exercise 11 Outputs: \n") 

pass_counter = 0
total_test = 0

lst=[4,5,6,7]
test_function = make_ends(lst)
print(test_function)

lst1=[10,5,60,70,2,1,4,9,578,35,0,7]
test_function = make_ends(lst1)
print(test_function)

lst2=[8]*1000
test_function = make_ends(lst2)
print(test_function)

print("\n")
actual1 = make_ends(lst)
print( "Testing make_ends(lst) ")
print( "Expected result: [4, 7], Actual result:", actual1)
total_test += 1
if actual1 == [4, 7]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual2 = make_ends(lst1)
print( "Testing make_ends(lst1) ")
print( "Expected result:[10, 7], Actual result:", actual2)
total_test += 1
if actual2 == [10, 7]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
  
actual3 = make_ends(lst2)
print( "Testing make_ends(lst2) ")
print( "Expected result: [8, 8], Actual result:", actual3)
total_test += 1
if actual3 == [8, 8]:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")  
 
print (pass_counter, "Tests passed for Exercise 11")
print (total_test-pass_counter,"Tests failed for Exercise 11") 

# Exercise 12
print ("\n Exercise 12 Outputs: \n") 

pass_counter = 0
total_test = 0

lst=[4,5]
test_function =  has23(lst)
print(test_function)

lst1=[2,2]
test_function =  has23(lst1)
print(test_function)

lst2=[1,3]
test_function =  has23(lst2)
print(test_function)

print("\n")
actual1 = has23(lst)
print( "Testing has23(lst) ")
print( "Expected result: False, Actual result:", actual1)
total_test += 1
if actual1 == False:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual2 = has23(lst1)
print( "Testing has23(lst1) ")
print( "Expected result: True, Actual result:", actual2)
total_test += 1
if actual2 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
  
actual3 = has23(lst2)
print( "Testing has23(lst2) ")
print( "Expected result: True, Actual result:", actual3)
total_test += 1
if actual3 == True:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")

print (pass_counter, "Tests passed for Exercise 12")
print (total_test-pass_counter,"Tests failed for Exercise 12") 

# No code below this line
print("\nEnd of file reached successfully")
