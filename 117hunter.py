a=input()
d=list(a)
#print(d)
j=0
summ=0
for i in range(0,len(d)):
    if d[i] !=0:
        summ=summ+int(d[i])**j 
        j=j+1
    else:
        summ=summ 
        j=j+1
    #print(summ)
print(summ)
