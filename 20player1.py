a=input()
lis=[]
for i in range(len(a)):
    t=a[i]
    e=ord(t)
    f=e+3
    if f>122:
        w=f-26
        d=chr(w)
        lis.append(d)
        #print(lis)
    elif f>90:
        w=f-26
        d=chr(w)
        lis.append(d)
        #print(lis)
    else:
        d=chr(f)
        lis.append(d)
print(''.join(list(lis)))
