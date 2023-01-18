class Rectangle:
    def __init__(self):
        self.__length=int(input("Enter the length:"))
        self.__width=int(input("Enter the width:"))
    def __lt__(self,obj2):
        area1=self.__length*self.__width
        area2=obj2.__length*obj2.__width
        print("Area of rectangle1 is",area1)
        print("Area of rectangle2 is",area2)
        return area1<area2
print("Enter length and width of 1st object:")
obj1=Rectangle()
print("Enter length and width of 2nd object:")
obj2=Rectangle()
if obj1<obj2:
    print("Rect1 is less than Rect2")
else:
    print("Rect1 is greater than Rect2")
        
    