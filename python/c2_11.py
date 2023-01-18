l=int(input("Enter length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
h=int(input("Enter the height "))
ar=lambda x,y:x*y
asq=lambda x: x*x
at=lambda x,y:0.5*x*y
print("Area of rectangle:",ar(l,b))
print("Area of square:",asq(l))
print("Area of triangle:",at(b,h))