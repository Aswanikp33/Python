a=int(input("Enter a:"))
b=int(input("Enter b:"))
#l=[10,20,30,40,50]
try:
    if b==0:
        raise Exception
    c=a/b
    print(c)
 # print(l[5])
except Exception as e:
    print("Exception raised")
'''    b=1
    c=a/b
    print(c)
else:
    print("No Exceptions")
finally:
    print("The 'try except' is finished")'''
'''marks=int(input("Enter the marks:"))
try:
      if marks<0 or marks>100:
          raise Exception("Marks should br in between 0 and 100")
      print("Marks =",marks)
except Exception as e:
    print(e)'''
class InvalidData(Exception):
    pass
class InvalidMarks(Exception):
    pass
marks=int(input("Enter the marks of student:"))
try:
    if marks<0 or marks>100:
        raise InvalidMarks
except InvalidMarks:
    print("Marks should br in between 0 and 100")
