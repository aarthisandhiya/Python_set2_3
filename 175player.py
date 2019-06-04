a=input()
b=input()
c=a+b 
#print(c)
c=list(c)
c.sort()
#print(c)
CIT=0
#print(len(c))
for i in range(0,len(c)):
    if len(c)<26 or c.count(c[i])>1:
        CIT=CIT+1 
if CIT==0:
    print("complementary")
else:
    print("non-complementary")
