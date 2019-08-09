a,b=map(str,input().split())
lis=[]
for i in b:
    if i in a and i not in lis:
        lis.append(i)
if len(lis)==len(b):
    print("".join(list(lis)))
