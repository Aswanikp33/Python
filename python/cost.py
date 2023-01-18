#find out he cost of a rectangular field with breadth(b=120),length(l=160).It cost x(2000 Rs per 1 sqr unit)
class rectangle:
    def __init__(self,length,breadth,unit_cost=0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost
    def get_perimeter(self):
        return 2 * (self.length + self.breadth)
    def get_area(self):
        return self.length * self.breadth
    def calculate_cost(self):
        area=self.get_area()
        return area * self.unit_cost
o=rectangle(160,120,2000)
print("Area of Rectangle:",(o.get_area()))
print("Cost of Rectangular field:",(o.calculate_cost()))
