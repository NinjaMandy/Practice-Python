#Program To find square root oF Number 

def SquareRoot(number):
    result = number**0.5   #  Used Exponentiation Operator (**)
    return result
    
number = int(input("Enter to find It\'s Square root"))
result = SquareRoot(number)
print(f"Number : {number} It\'s Square root :{result} ") #used F-String Here
