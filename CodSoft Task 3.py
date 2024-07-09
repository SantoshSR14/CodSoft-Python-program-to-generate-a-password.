import random
import string
print("Password type:\n1.Numbers\n2.Alphabets\n3.Punctuations\n4.Combination of all three")
a=int(input("Enter Password type:"))
b=int(input("Enter password length:"))
c=""
if(a==1):
    c+=string.digits
elif(a==2):
    c+=string.ascii_letters
elif(a==3):
    c+=string.punctuation
else:
    c+=string.digits
    c+=string.punctuation
    c+=string.ascii_letters
d=[]
for i in range(b):
    password=random.choice(c)
    d.append(password)
print("Generated password:"+"".join(d))
    
