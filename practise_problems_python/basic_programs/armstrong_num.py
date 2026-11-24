
# Python Program to Check Armstrong Number

# Using a Mathematical Approach
n=int(input('Enter number : '))
t=n
power=len(str(n))
s=0

while t > 0:
    digit = t %10
    s+=digit ** power
    t//=10

if s==n:
    print("Armstrong Number.")    
else:
    print("Not an Armstrong Number")   