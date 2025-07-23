#Level 1 :Task 1
#Task: String Reversal
'''
 Create a Python function that takes a string as input and returns the reverse of that string.
 For example, if the input is "hello," the function should return "olleh."
'''

class L1Task1:
    def string_reversal(str):
        #print(str[::-1])
        temp=""
        l=len(str)
        for i in range(l-1,-1,-1):
            temp=temp+str[i]
        for j in temp:
            print(j,end="")
str=input("Enter Number to Reverse: ")
obj1=L1Task1
obj1.string_reversal(str)