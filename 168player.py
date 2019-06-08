a=input()
b=''
for x in range(1,len(a)):
    if(a[x].isnumeric()):
        b=b+(a[x-1]*int(a[x]))
print(b)
