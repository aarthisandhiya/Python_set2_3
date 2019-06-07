a=input()
lis=[]
for i in a:
    if i not in lis:
        lis.append(i)
        #print(i)
    else:
        break
print(len(lis))
