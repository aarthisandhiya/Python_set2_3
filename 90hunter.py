a=input()
dict={}
for i in range(0,len(a)):
    c=a.count(a[i])
    dict.update({a[i]:c})
#print(dict)
h=0
for k,j in dict.items():
    if j>h:
        h=j 
        it=k 
print(it,h)
    
