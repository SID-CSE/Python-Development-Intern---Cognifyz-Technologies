#Level 1 :Task 2
#Task: Temperature Conversion
'''
 Create a Python program that converts temperatures between Celsius and Fahrenheit.
 Prompt the user to enter a temperature value and the unit of measurement,
 and then display the converted temperature.
'''

class L1Task2:
    def __init__(self,Tvalue,Tunit):
        Tvalue=self.Tvalue
        Tunit=self.Tunit
    def toFahrenheit(Tvalue):
        Tvalue=(float(Tvalue)*(9/5)+32)
        print(Tvalue,"F")
    def toCelsius(Tvalue):
        Tvalue=(float(Tvalue)-32)*(5/9)
        print(Tvalue,"C")

Tvalue,Tunit=input("Input Temperature with Unit in Format - Value Unit : ").split(" ")
obj1=L1Task2
if Tunit=="C":
    obj1.toFahrenheit(Tvalue)
elif Tunit=="F":
    obj1.toCelsius(Tvalue)
else:
    print("Input Format is Incorrect")

