from math import e
import random
import string

print('Starting Password Generation Tool')

length = int(input('\nEnter the length of password: '))

if length <= 0:
    print("Value of password to short")
    exit
    
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

complexity = int(input('\nEnter the Complexity on a scale of 1-4: '))

if complexity == 1:
    all = lower
elif complexity == 2:
    all = lower + upper
elif complexity == 3:
    all = lower + upper + num
elif complexity == 4:
    all = lower + upper + num + symbols
else:
    print("Invalid Complexity selected")
    exit
    
password = "".join(random.sample(all,length))

print(password)
