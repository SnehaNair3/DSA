
# A = P(1 + R/100)^t 
# Compound Interest = A - P


# Using Exponentiation Operator
P = 1200   
R = 5.4    
T = 2 
A=P * (1+R/100)**T
CI=A-P
print("Compound interest:", CI)

# Using Built-in pow() Function
p = 10000
r = 10.25
t = 5
Amt=p* (pow(1+r/100,t))
ci=Amt-p
print("Compound interest:", ci)