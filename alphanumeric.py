x=input()
c=0
for i in range(0,len(x)):
	if x[i].isalnum():
		break
	else:
		c=c+1
print(c)
