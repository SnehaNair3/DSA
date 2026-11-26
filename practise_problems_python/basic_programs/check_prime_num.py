
n=int(input("Enter a number : "))

# Using flag variable 
if n <=1:
    print("False")
else:
    prime=True
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            prime=False
            break
    print(prime)  



# Using isprime() method 
# isprime() function from the SymPy library to check whether a number is prime.
from sympy import isprime
print(isprime(n))    


# Using Sieve of Eratosthenes
