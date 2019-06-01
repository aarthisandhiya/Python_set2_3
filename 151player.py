a=input()
c=0
for i in range(0,len(a)):
    if a[i]=='a' or a[i]=='b':
        c=c+1
if c==len(a) or c==len(a)-1:
    print("yes")
else:
    print("no")
