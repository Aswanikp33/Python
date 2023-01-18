#overloading.py
'''A="hello"
B=" How are you?"
print(A+B)
C=10
D=20
print(C+D)'''
# methodover.py
'''class moverload:
    def display(self,a=None,b="Done"):
         print(a,b)
obj=moverload()
obj.display()
obj.display(10)
obj.display(10,20)'''
#mthdridding.py
'''class father():
    def transportation(self):
        print("Cycle")
class son(father):
    def transportation(self):
        print("Bike")
obj=son()
obj.transportation()'''
#encap.py
'''class encap:
    __a=10
    def __display(self):
        print("Welcome",self.__a)
    def   show(self):
        print("hi")
        self.__display()
obj=encap()
#print(obj.a)
# obj.display()
obj.show()'''
#abstrctclass.py
from abc import ABC,abstractmethod
class Aclass(ABC):                         #abstract class                 
    @abstractmethod                       #decoder
    def display(self):                         #abstract method
        None
    @abstractmethod
    def display(self):                        
        None
class Demo(Aclass):                        #concrete class
    def display(self):
        print("Abstract Methods")
    def show(self):
        print()
obj=Demo()
#obj.display()
obj.show()
