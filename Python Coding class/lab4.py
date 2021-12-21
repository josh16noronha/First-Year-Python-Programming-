# Lab Number: 16A

# Name and Student Number: Joshua Noronha, 101194076

# Functions below this line:
import math
def area_of_disk(radius):
 return math.pi * radius ** 2
def area_of_ring(outer, inner):
 return area_of_disk(outer) - area_of_disk(inner)

LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934
def convert_to_litres_per_100_km(mpg):
 return 100 * LITRES_PER_GALLON / KMS_PER_MILE / mpg

def accumulated_amount(principal, rate, n, time):
 return principal*(1+ rate / n)**(n * time)

def area_of_cone(height, radius):
 return math.pi * radius * math.sqrt((radius**2)+(height**2))

# Main Script below this line:

# Exercise 1
print ("\n Exercise 1 Outputs: \n") 

area = area_of_disk(5)
print(area)
area = area_of_disk(5.0)
print(area)
area = area_of_ring(10, 5)
print(area)
area = area_of_ring(10.0, 5.0)
print(area)

# Exercise 2
print ("\n Exercise 2 Outputs: \n")

mpg = convert_to_litres_per_100_km(32)      # 32 mpg
print(mpg)
# mpg = convert_to_litres_per_100_km(0)     # 0 mpg (This gives a math error, the only way to resolve this was to comment the call ,                                                   and print function)
# print(mpg)
print("When the parameter mpg is 0 the output is a math error")
mpg = convert_to_litres_per_100_km(5.6785)  # 5.6785 mpg (Real number)
print(mpg)
mpg = convert_to_litres_per_100_km(10)      # 10 mpg (integer)
print(mpg)

# Exercise 3
print ("\n Exercise 3 Outputs: \n")

amount = accumulated_amount(1500, 0.043, 4, 6) # principal is $1500, rate is 4.3%, n is 4 years, time is 6 years  "Simple value trial"
print(amount)
amount = accumulated_amount(10, 0.010, 2, 2) # principal is $10, rate is 1.0%, n is 2 years, time is 2 years  "Simple value trial"
print(amount)
amount = accumulated_amount(0, 0.010, 2, 2)    # principal is $0, rate is 1.0%, n is 2 years, time is 2 years   "boundary values trial"
print(amount)
amount = accumulated_amount(1500, 0, 2, 2)     # principal is $1500, rate is 0%, n is 2 years, time is 2 years  "boundary values trial"
print(amount)

# Exercise 4
print ("\n Exercise 4 Outputs: \n")

Cone_Area = area_of_cone(5, 3)     # height is 5, radius is 3 (integers)
print(Cone_Area)
Cone_Area = area_of_cone(8, 20.0)  # height is 8, radius is 20 (mix of integer and float)
print(Cone_Area)
Cone_Area = area_of_cone(7.1, 6.0)   # height is 7.1, radius is 6.0 (floats)
print(Cone_Area)

# No code below this line
print("\nEnd of file reached successfully")