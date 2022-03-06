#Finding Roots of  Quadatice Equation  
import math 
def findRoot(valueList):
    a = valueList[0]
    b = valueList[1]
    c = valueList[2]
    
    d = b*b - 4*a*c
    print(f"The Given Values In Equation a:{a}, b:{b},c:{c}")
    if d>0: 
        rootPart = math.sqrt(d)
        root1 = (-b + rootPart)/2*a
        root2 = (-b - rootPart)/2*a
        print(f" Roots Of the Equation: {root1} and {root2}")
    elif d==0:
        root= -b/2*a
        print(f" both Root will Be Equal which is : {root}")
    else: 
        print(" No real roots For this Equation.")
   
    
    
valueList = [int(item) for item in input("Enter a,b and c Values Separated by Space").strip().split()]
findRoot(valueList)
