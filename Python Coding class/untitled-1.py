def abc(a:bool, b:float)->int:
    return 
 









def convert(km: float) -> str:
    """
    Returns a string containing the length in miles and yards
    that is equivalent to km kilometers.
    Note that there are 1760 yards in a mile, and 1 mile is 1.6093 km.
    Assume that km is non-negative (error checking is not required).
    >>> convert(5)
    '3 miles and 188.22 yards' 
            # it is fine if it returns something like:
            # '3.0 miles and 188.21599..... yards' for all examples
    >>> convert(0)
    '0 miles and 0.0 yards'
    >>> convert(1.6102144)
    '1 miles and 1.0 yards' # don't worry about singular/plural 
    """
  #a= km//1.6093
   #b=km//1.6093*1760
    return km//1.6093,"miles and",(km//1.6093)*1760
Testcase=convert(5)
#print(Testcase)
Testcase=convert(0)
#print(Testcase)
Testcase=convert(1.6102144)
#print(Testcase)




import math 
def length_of_chord(line:float,radius:float)->float:
    """
    Returns the length of the chord using the parameters of line and radius 
    >>>length_of_chord(0,2)
    4.0
    >>>length_of_chord(1.26,3.55)
    6.637740579444183
    >>>length_of_chord(85,700.5)
    1390.647690826113
    """
    return 2*math.sqrt(radius**2-(line**2))

Test1=length_of_chord(0,2)
#print(Test1)
Test1=length_of_chord(1.26,3.55)
#print(Test1)
Test1=length_of_chord(85,700.5)
#print(Test1)


def growth_of_pig(common_weight: float, target_rate: float, pig1_growth_rate: float, pig2_growth_rate: float)->list:
    """
    Returns the number of weeks it takes for pig1's weight to become pig1_growth_rate bigger than the second pig. The parameters that are used are common_weight , target_rate, pig1_growth_rate, pig2_growth_rate
    Some assumptions are that all the rate values are between 0.0 to 100.0 , the farmers are constantly feeding the pigs equally, the first pig's growth rate is always more than pig 2's growth rate. The initial mass cannot be 0
   
   >>>growth_of_pig(100,33.3,5.5,2.8)
   [12, 50.832]
   >>>growth_of_pig(120,33.3,33.3,2.8)
   [2, 86.413]
   >>>growth_of_pig(200,45.8,1.5,0.8)
   [55, 7.18]
   """
    # Using a modified version of the compounding intrest formula
    lst=[]
    pig1_mass= common_weight
    pig2_mass= common_weight
    num_of_weeks=0
    while pig2_mass*(1+(target_rate/100)) > pig1_mass: 
        pig1_mass += (pig1_growth_rate/100)* (pig1_mass)
        pig2_mass += (pig2_growth_rate/100) * (pig2_mass)
        num_of_weeks += 1
        #lst+=[num_of_weeks,round(pig1_mass-pig2_mass,2)]
    return [num_of_weeks,round(pig1_mass-pig2_mass,3)]
    
test=growth_of_pig(100,33.3,5.5,2.8)
#print(test)
test1=growth_of_pig(120,33.3,33.3,2.8)
#print(test1)
test2=growth_of_pig(10,45.8,1.5,0.8)
#print(test2)


def loop_function(size:int, start:int, operation:bool)->list:
    """
    >>>
    
    >>>
    
    >>>
    
    """
    lst=[]
    for i in range(0,size-1):
        lst+=[start]
        lst+=[start+1]
        if operation== True:
            i+=lst[i-1] 
            i+=lst[i-2]
        elif operation== False:
            i-=lst[i-1]
            i-=lst[i-2]
    return lst
    
test=loop_function(5,-1,True)
#print(test)
test1=loop_function(6,5,False) 
#print(test1)
test2=loop_function(9,2,False) 
#print(test1)
        
def print_strs(my_set:set)->int:
    """
    """
    for i in my_set:
        if (type(i))==str:
            print (i)
test=print_strs({1,4.5,"cherry"})
print(test)
test1=print_strs({1,4.5,"cherry","melon"})
print(test1)
test2=print_strs({1,3,4,8})
print(test2)


