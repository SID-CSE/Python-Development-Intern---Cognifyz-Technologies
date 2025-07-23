#Level 1 :Task 3
#Task: Palindrome Checker
'''
 Write a Python function that checks whether a given string is a palindrome.
 A palindrome is a word, phrase, or sequence that reads the same backward as forward
 (e.g., "madam" or "racecar").
'''

class L1Task5:
    def __init__(self,str):
        str=self.str
    def Check(str):
        rev=""
        l=len(str)
        for i in range(l-1,-1,-1):
            rev=rev+str[i]
        if str==rev:
            print("Palindrome")
        else:
            print("Not Palindrome")


str=input("Enter a word, phrase, or sequence to check : ")
obj=L1Task5
obj.Check(str)