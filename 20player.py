a=input()
lis=[]
for i in range(len(a)):
    t=a[i]
    e=ord(t)
    f=e+3
    d=chr(f)
    lis.append(d)
print(''.join(list(lis)))
