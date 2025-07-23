# Level 2 :Task 3
# Task: Password Strength Checker
'''
 Create a Python function that evaluates the strength of a password entered by the user.
 Implement checks for factors such as length, presence of uppercase and lowercase letters,
 digits, and special characters.
'''
class L2Task3:
    def Checker(password):
        digits=['1','2','3','4','5','6','7','8','9','0']
        s_char=["!","@","#","$","%","^","&","*","/","?","+","_"]
        d=c=u=l=False
        for i in password:
            if i in digits:
                d=True
            if i in s_char:
                c=True
            if i.islower():
                l=True
            if i.isupper():
                u=True
        le=len(password)
        if d and c and u and l and le>=10:
            print("Strong Password")
        else :
            print("Weak Password : Use combination of Upper and Lower Case characters , with Numbers and Special Characters with a minimum length of 10")
password=input("Enter Password : ")
obj=L2Task3
obj.Checker(password)