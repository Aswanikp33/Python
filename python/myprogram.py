import myfunctions

x=int(input("Enter the first Element:"))
y=int(input("Enter the second element:"))
choice=int(input("Enter the choice: 1.Addition\ 2.Substraction\ 3.Multiplication\ 4.Division:"))
if choice==1:
    sum=myfunctions.sum(x,y)
    print("sum of two numbers:",sum)
elif choice==2:
    print("sub of two numbers:",sub(x,y))
elif choice==3:
    print("mul of two numbers:",sub(x,y))
elif choice==4:
    print("div of two numbers:",sub(x,y))
else:
    print("Invalid Input")
    



