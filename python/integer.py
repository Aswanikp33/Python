l1=[1,2,3,4,5]
l2=[2,3,10]
'''sum1=0
for i in l1:
    sum1=sum1+i
sum2=0
for i in l2:
    sum2=sum2+i
if len(l1)==len(l2):
    print("Length of list are same")
else:
    print("Length of list are not same")
if sum1==sum2:
    print("Sums of list are equal")
else:
    print("Sums of list are not equal")'''
for i in l1:
    for j in l2:
        if i==j:
            print("Common element is",i)