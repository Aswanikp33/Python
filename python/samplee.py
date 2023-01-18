'''fn=open("newfile.txt",'r')
s=fn.readline()
print(s)
fn.close()
print(fn.closed)
print(fn.mode)
print(fn.name)'''
fo=open("a.txt","w")
fo.write("Python is a great language.\n Yeah its great!!!\n");
fo.close()
fo=open("a.txt","r")
str=fo.read();
print("Read string is:",str)
fo.close()


