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

def average(lst: list)->list:
    """
    Returns a new list of tuples which has three numbers in each tuple that are avarage values of the values in the original list. The parameter is lst and an assumption that can be made is that the tuples cannot be negative integers. 
    
    >>>average([(1,2,3),(4,5,6),(7,8,9)])
    [(2, 2, 2), (5, 5, 5), (8, 8, 8)]
    >>>average([(41,27,3),(4,65,6)])
    [(23, 23, 23), (25, 25, 25)]
    >>>average([(0,0,0),(0,0,0)])
    [(0, 0, 0), (0, 0, 0)]
    """
    new_list=[]
    for tupl in lst:
        avarage = (tupl[0]+tupl[1]+tupl[2]) // 3
        new_list += [(avarage,avarage,avarage)]
    return new_list
      
    
def sum_x(n: set)->float:
    """
    Ruturns the sum of all the x coordinates using the set of tuples subbed into the n parameter.
    An assumption is that the tuples cannot be empty
    
    >>>sum_x({(5.0,6.5),(5.8,64),(25,87)})
    35.8
    >>>sum_x({(0,0),(0,0),(0,0)})
    0
    >>>sum_x({(9.56,7.5),(5.8,65.4),(25.5,8.77)})
    40.86
    """
    addition=0
    for tupl in n:
        addition += tupl[0]
    return addition
    


# Main Script below this line:

# Exercise 1

# Step 1 Question: What is displayed when Python evaluates point1?

# Answer: The output for the print statement of point1 is a list that contains the two points of 1.0 and 2.0 as so [1.0, 2.0]

# Step 2 Question: What is displayed when Python evaluates point1?

# Answer: When the .append(3.0) function is used for point1, what happens is that the lenth of the list expands from two points to three points, so the 3.0 is placed after the first two points as so [1.0, 2.0, 3.0] 

# Question: What is displayed each time Python evaluates point1?

# Answer1: After python runs point1.pop(0) the item at index 0 in the point1 list which is 1.0 gets taken out of the list and after point1 is printed then 2.0 is moved to index 0 in the list and 3.0 moved to index 1 so the two values in the list is [2.0, 3.0]

# Answer2: After python runs point1.pop() the last item in the list gets taken out of the list so now the only value in the list is [2.0] after point1 is printed

# Step 3 Question: What is displayed when the last two statements are evaluated? 

# Answer: When type(point1) is outputed the class is identified as a truple. When point1 is printed two points are placed in the truple such as (1.0, 2.0) 

# Step 4 Question: What is displayed when Python evaluates x and y?

# Answer1: When python evaluates x which is binded to point1[0] but since index 0 contains 1.0 so that is what gets outputed. When python evaluates y which is binded to point1[1] but since index 1 contains 2.0 so that is what gets outputed.

# Answer2: When python evaluates x which is binded to the x coordinate of (x,y) since the coordinate of x is 4.0 this becomes the float value that gets outputed. When python evaluates y which is binded to the y coordinate of (x,y) since the coordinate of y is 6.0 this becomes the float value that gets outputed.

# Step 5 Question: What is displayed when Python executes each statement? 

# Answer:

#  point2[0] = 2.0            # Can we change the point to (2.0, 6.0)?
# No, I was not able to change my point to (2.0, 6.0) because I am getting an error statement saying "'tuple' object does not support item assignment" thus proving that you can't replace items in a tuple. 

# OUTPUT:
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'tuple' object does not support item assignment

# point2.append(4.0)                # Can we add a third coordinate?
# No, I was not able to add a third coordinate of 4.0 because I am getting an error statement saying "'tuple' object has no attribute 'append'" thus proving that you can't add items in a tuple. 

# OUTPUT:
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'tuple' object has no attribute 'append'

# point2.pop(0)                     # Can we remove the first coordinate?
# No, I was not able to remove the first coordinate of 0 because I am getting an error statement saying "'tuple' object has no attribute 'pop'" thus proving that you can't remove items in a tuple. 

# OUTPUT:
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'tuple' object has no attribute 'pop'

# Step 6 Question: Try this experiment

# Answer:

# points = [(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)]
# points[0]  # This prints (1.0, 5.0)
# points[1]  # This prints (2.0, 8.0)
# points[2]  # This prints (3.5, 12.5)

# Exercise 2
print ("\n Exercise 2 Outputs: \n") 

pass_counter = 0
total_test = 0

lst=[(1,2,3),(4,5,6),(7,8,9)]
test_function = average(lst)
print(test_function)


lst1=([(41,27,3),(4,65,6)])
test_function = average(lst1)
print(test_function)

lst2=([(0,0,0),(0,0,0)])
test_function = average(lst2)
print(test_function)

print("\n")
actual = average(lst)
print( "Testing average(lst) ")
print( "Expected result: [(2, 2, 2), (5, 5, 5), (8, 8, 8)], Actual result:", actual)
total_test += 1
if actual == [(2, 2, 2), (5, 5, 5), (8, 8, 8)]:
    print ("Test passed")
    pass_counter += 1
else:
    print ("Test failed")
    
actual = average(lst1)
print( "Testing average(lst1) ")
print( "Expected result: [(23, 23, 23), (25, 25, 25)], Actual result:", actual)
total_test += 1
if actual == [(23, 23, 23), (25, 25, 25)]:
    print ("Test passed")
    pass_counter += 1
else:
    print ("Test failed")
        
actual = average(lst2)
print( "Testing average(lst2) ")
print( "Expected result: [(0, 0, 0), (0, 0, 0)], Actual result:", actual)
total_test += 1
if actual == [(0, 0, 0), (0, 0, 0)]:
    print ("Test passed")
    pass_counter += 1
else:
    print ("Test failed")        
    
    
print (pass_counter, "Tests passed for Exercise 2")
print (total_test-pass_counter,"Tests failed for Exercise 2")    

# Exercise 3

# Step 1 Question: What is displayed when points is evaluated?

# Answer: {(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)} is displayed when points is evaluated, in sets the order does not matter so that is why it does not look like how it should when it was initialized as so  points = {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)}

# Question: What is displayed when points is evaluated? 

# Answer: {(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)} is displayed when points is evaluated, in sets the order does not matter so that is why it does not look like how it should when the order is established as points = {point1, point2, point3}

# Question:  What is displayed when points is evaluated?

# Answer: {(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)} is displayed when tuples are added into an empty set, this works because sets are mutable so in the set we can add points to make the sets bigger.

# Step 2 Question: How many copies of point (4.0, 6.0) are in the set?

# Answer: There is only one copy of the point (4.0, 6.0) in the set, because sets do not chave any duplicates

# Step 3 Question: What is displayed when points[0] is evaluated?

# Answer: When points[0] is evaluated an error statement is isplayed saying "'set' object is not subscriptable"

# Step 3 Question: What is displayed when this loop is executed?

# Answer: All the points in the set are displayed when the loop is executed.

#OUTPUT
# (4.0, 6.0)
#(1.0, 2.0)
#(10.0, -2.0)

# Exercise 4
print ("\n Exercise 4 Outputs: \n") 

pass_counter = 0
total_test = 0

n={(5.0,6.5),(5.8,64),(25,87)}
b= sum_x(n)
print(b)

n1={(0,0),(0,0),(0,0)}
b= sum_x(n1)
print(b)

n2={(9.56,7.5),(5.8,65.4),(25.5,8.77)}
b= sum_x(n2)
print(b)

print("\n")
actual = sum_x(n)
print( "Testing sum_x(n) ")
print( "Expected result: 35.8, Actual result:", actual)
total_test += 1
if actual == 35.8:
    print ("Test passed")
    pass_counter += 1
else:
    print ("Test failed")

actual = sum_x(n1)
print( "Testing sum_x(n1) ")
print( "Expected result: 0, Actual result:", actual)
total_test += 1
if actual == 0:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")
 
actual = sum_x(n2)
print( "Testing sum_x(n2) ")
print( "Expected result: 40.86, Actual result:", actual)
total_test += 1
if actual == 40.86:
 print ("Test passed")
 pass_counter += 1
else:
 print ("Test failed")


print (pass_counter, "Tests passed for Exercise 4")
print (total_test-pass_counter,"Tests failed for Exercise 4")   





























