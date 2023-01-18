from math import sqrt
n=int(input("Enter a limit:"))
for i in range(1000,n):
    if sqrt(i)==int(sqrt(i)) and 1%2==0:
          print(i)