dic1={'just':20,'such':19}
dic2={'a':10,'b':9}
# print(dic1|dic2)
#print({**dic1,**dic2})
dic3=dic2.copy()
dic3.update(dic1)
print(dic3)


