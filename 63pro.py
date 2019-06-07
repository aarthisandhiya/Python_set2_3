a=input()
lis=[]
if len(a)==1:
    print("1")
elif len(a)==2:
    s=a[0]
    h=a[1]
    if s==h:
        print("1")
    else:
        print("2")
else:
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]!=a[j] and a[i] not in lis:
                lis.append(a[i])
    print(len(lis)+1)
