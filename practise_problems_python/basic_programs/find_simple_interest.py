
# Using function
def simple_interest(p,t,r):
    return (p*t*r)/100

result=simple_interest(1000,2,5)
print(result)


# Using Function with User Input
def simple_interest2(p,t,r):
    return (p*t*r)/100

p1=float(input("Enter principal: "))
t1=float(input("Enter time: "))
r1=float(input("Enter rate: "))

res=simple_interest2(p1,t1,r1)
print(res)


# Using lambda function
si=lambda p2,t2,r2: (p2*t2*r2)/100
res2=si(8,6,8)
print(res2)


# Using list comprehension
p3,t3,r3=8,6,8

si3=[p3*t3*r3/100][0]
print(si3)