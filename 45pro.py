a=int(input())
a=str(a)
lis=[]
d=a[::-1]
if a==d:
    print("yes")
else:
    a=str(a)
    lis.append(a)
    for i in range(0,len(a)):
        lis.insert(0,'0')
        o=''.join(list(lis))
        s=o[::-1]
        #print(s,"====","s")
        if o==s:
            
            print("yes")
            break 
    else:
        print("no")
    
    
