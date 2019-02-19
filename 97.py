number=int(input())
c=0
while number>0:
	b=number%10
	c=c*10+b
	number=number//10
	
print(c)
