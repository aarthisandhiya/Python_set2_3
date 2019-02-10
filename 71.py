x =input()
w = "" 
for i in x: 
    w = i + w 
    if (x==w): 
        print("yes") 
        break
else:
    print("no")
