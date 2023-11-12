#CALCULATOR PROGRAM
number1=int(input("enter first number:"))
number2=int(input("enter second number:"))
operator=input("enter any operator (+,-,*,/,%):")
def calculator(number1, number2, operator):
    if(operator == "+"):
        print("The addition of number1 and number2 is ",number1 + number2)
        return
    if(operator == '-'):
        print("The subtraction of number1 and number2 is ", number1 - number2)
        return
    if(operator == "*"):
        print("The multiplication of number1 and number2 is ", number1 * number2)
        return
    if(operator == "/"):
        print("The division of number1 and number2 is ", number1 / number2)
        return
    if(operator == "%"):
        print("The modulus of number1 and number2 is ", number1 % number2)
        return
    else:
        print("Invalid input")
        return
calculator(number1,number2,operator)
