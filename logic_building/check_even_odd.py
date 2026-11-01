
# Naive Approach
def isEven(n):
    if n%2 ==0:
        return True
    else:
        return False

#Efficient Approach
# The last bit of all odd number is always 1 , while for even numbers its 0.
# Perform BITWISE AND with 1 , odd numbers gives 1 and even numbers give 0.
def isEven2(n):
    if (n&1) ==0:
        return True
    else:
        return False
    

if __name__ =="__main__":
    print(isEven(15))    
    print(isEven(44))  
    print('----------------')
    print(isEven2(13))  
    print(isEven2(23))  
    print(isEven2(24))  
