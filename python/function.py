def sum(a,b):
        "adding two numbers a and b"
        sum=a+b
        return sum
def sub(a,b):
        "substracting two numbers a and b"
        sub=a-b
        return sub
def mul(a,b):
        "multiply two numbers a and b"
        mul=a*b
        return mul
def div(a,b):
        "dividing two numbers a and b"
        div=a/b
        return div
x=int(input("Enter the first Element:"))
y=int(input("Enter the second element:"))
choice=int(input("Enter the choice: 1.Addition\ 2.Substraction\ 3.Multiplication\ 4.Division:"))
if choice==1:
    print("sum of two numbers:",sum(x,y))
elif choice==2:
    print("sub of two numbers:",sub(x,y))
elif choice==3:
    print("mul of two numbers:",sub(x,y))
elif choice==4:
    print("div of two numbers:",sub(x,y))
else:
    print("Invalid Input")
    
    
    

