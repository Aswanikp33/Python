a=int(input("Enter a limit:"))
for i in range(1,a+1):
    for j in range(0,i+1):
        a=i*j
        if a==0:
            continue
        else:
            print(a,end=" ")
    print("\n")