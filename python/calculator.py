def sum (a,b):
    "addition two number a and b"
    sum=a+b
    return sum


def sub (a,b):
    "subtracting two number a and b"
    sum=a-b
    return sum


def mul (a,b):
    "multiply two number a and b"
    sum=a*b
    return sum


def div (a,b):
    "adding two number a and b"
    div=a/b
    return sum
a=int(input("Enter the first element:"))
b=int(input("Enter the second element:"))
choice=int(input("Enter the choice\n1.Addition\n2.substraction\n3.multiplication\n4division:"))
if choice==1:
   print("sum is",sum(a,b))
elif choice==2:
     print("substraction is",sub(a,b))
elif choice==3:
     print("multiplication is",mul(a,b))
elif choice==2:
     print("division is",div(a,b))
else:
     print("invalid choice")
   
   
   
   