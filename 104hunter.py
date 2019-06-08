a=int(input())
summ=0
b=str(a)
s=[]
for i in range(0,len(b)):
    summ=summ+int(b[i])
    s.append(summ)
print(sum(s))
        
