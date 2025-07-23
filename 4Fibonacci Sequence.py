# Level 2 :Task 4
# Task: Fibonacci Sequence
'''
 Write a Python function that generates the Fibonacci sequence up to a given number of terms.
 The function should take an integer input from the user and display the Fibonacci sequence up to that number of terms.
'''

class L2Task4:
    def Fibbonaci(n):
        res=[]
        a, b= 0,1
        for i in range(n):
            res.append(a)
            a,b=b,a+b
        print(f"Fibonacci Series of {n} terms : {res}")
n=int(input("Enter Number : "))
obj=L2Task4
obj.Fibbonaci(n)
