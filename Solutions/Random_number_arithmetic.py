 #must  for genrating random   Number
import random  

# Function to perform Arithmetic Operation
def arithmeticOperation(num1, num2): 
    sum = num1+num2
    print(f"sum : {sum}")
    sub = num1-num2
    print(f"substraction: {sub}")
    div = num1/num2
    print(f"Division : {round(div,2)}")
    mul = num1*num2
    print(f"Multiplication : {mul}")

#function to Generate Random Number 
def GenerateRandomNumber(start , limit):
    num1 = random.randint(start , limit+1)
    num2 = random.randint(start , limit+1)
    print(f"The Number Generated :  {num1} and {num2},\n")
    arithmeticOperation(num1, num2)
   
    
# here can set The limits for Number Generation    
GenerateRandomNumber(10,20)
