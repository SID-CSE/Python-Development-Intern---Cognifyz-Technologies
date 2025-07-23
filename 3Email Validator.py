#Level 1 :Task 3
#Task: Email Validator
'''Develop a Python function that validates whether a given string is a valid email address.
Implement checks for the format, including the presence of an "@" symbol and a domain name
'''
class L1Task4:
    def __init__(self,email):
        email=self.email
    def email_check(email):
        address,domain=email.split("@")
        if '@' in email and  domain in Domain:
            print("Valid Email")
        else:
            print("Invalid Email")

Domain=['gmail.com','yahoo.com','hotmail.com','live.com','outlook.com','googlemail.com']
email=input("Enter Email Address to Check : ")
obj1=L1Task4
obj1.email_check(email)