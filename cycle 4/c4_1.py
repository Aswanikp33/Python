class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def get_perimeter(self):
        return 2 * (self.length + self.breadth)
    def get_area(self):
        return self.length * self.breadth
    def compare(self,s):
         try:
             if r.get_area()==s.get_area():
                 print("Both have equal area")
             elif r.get_area()>s.get_area():
                  print("Largest is:",r.get_area())
             else:
                  print("Largest is:",s.get_area())
         except:
               print("No Exception")
l1=int(input("Enter length of first rectangle:"))
b1=int(input("Enter breadth of first rectangle:"))
l2=int(input("Enter length of second rectangle:"))
b2=int(input("Enter length of second rectangle:"))
r=rectangle(l1,b1)
print("Area of Rectangle:",(r.get_area()))
print("Perimeter of Rectangle:",(r.get_perimeter()))
s=rectangle(l2,b2)
print("Area of Rectangle:",(s.get_area()))
print("Perimeter of Rectangle:",(s.get_perimeter()))
r.compare(s)
        
            
