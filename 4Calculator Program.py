#Level 1 :Task 3
#Task: Calculator Program
'''
 Create a Python program that acts as a basic calculator.
 It should prompt the user to enter two numbers and an operator(+, -, *, /, % ),
 and then display the result of the operation.
'''

num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))
op=input("Enter Operand : ")
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
elif op=='%':
    print(num1%num2)
else:
    print("Operation is Not Valid")