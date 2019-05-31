a=int(input())
c=0
for i in range(1,a+1):
    if a%3==0 and c<a:
        c=c+3 
    elif a%7==0 and c<a:
        c=c+7
    elif a%10==0 and c<a:
        c=c+3+7 
if (c==a):
    print("yes")
else:
    print("no")
