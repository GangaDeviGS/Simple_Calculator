# Simple Calculator
# First create def functions for Addition
# Subtraction
# Division
# Multiplication

# def function for Addition
def add (x,y):
    return x+y

# def function for Subtraction
def subtract (x,y):
    return x-y

# def function for Division
def divide (x,y):
    return x/y

# def function for multiplication
def multiply (x,y):
    return x*y

# Now print the options for Arithmetic Operations
'''print ("\t SIMPLE CALCULATOR \n \n 
Select Operation \n 
1.Add \n
2.Subtract \n 
3.Divide \n
4.Multiply'''

# You can use this method for single line command
# or use below method
print ("\t SIMPLE CALCULATOR \n")
print ("Select Operation") 
print ("1.Add")
print ("2.Subtract") 
print ("3.Divide")
print ("4.Multiply")

# Now create a while loop
while True:
    # Ask what operation want to functionate
    operation = input("Select one choice (1/2/3/4) : ")

    # Create "if condition"  to check input is valid
    if operation in ('1', '2', '3', '4') :
        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))
        except ValueError :
            print ("INVALID INPUT,ENTER A VALID NUMBER")
            continue 

        if operation == "1" :
            print (num1, "+" ,num2, "=" ,add(num1,num2))

        elif operation == "2" :
            print (num1, "-" ,num2, "=" ,subtract(num1,num2))

        elif operation == "3" :
            print (num1, "/" ,num2, "=" ,divide(num1,num2)) 

        elif operation == "4" :
            print (num1, "*" ,num2, "=" ,multiply(num1,num2))

        # Check user want another calculation
        # Break the while loop if answer is no
        next_Question  = input("Let's do next calculation? (yes/no) : ")
        if next_Question == "no" :
            break
    else:
        print("Invalid Input")        




        