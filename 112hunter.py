a=input()
b=input()
s=[]
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j] and j<=i:
            if a[i] not in s:
                s.append(a[i])
print(''.join(list(s)))
