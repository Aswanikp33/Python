'''n=int(input("Enter a number: "))    
factorial = 1    
for i in range(1, n+1):
    factorial=factorial*i
print("The factorial is:",factorial)'''
def calc_factorial(x):
    if x==1:
        return 1
    else:
        return(x*calc_factorial(x-1))
n=int(input("Enter a value:"))
print("The factorial of",n,"is",calc_factorial(n))