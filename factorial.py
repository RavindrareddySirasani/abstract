def display(n):
    if n==0 or n==1:
        return 1
    else:
        return n*display(n-1)
n=int(input("enter your value:")
print("the result is:",display(n))      
