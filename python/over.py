n=int(input("Enter the number of elements:"))
list1=[]
for i in range(n):
    number=int(input("Enter the number:"))
    if number>=100:
        list1.append('over')
    else:
        list1.append(number)
print("the output is:",list1)
                        
