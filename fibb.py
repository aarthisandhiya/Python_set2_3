a=1
b=1
i=1
n=int(input())
print(a,b,end=" ")
while i<n-1:
	c=a+b
	print(c,end=" ")
	a=b
	b=c
	i=i+1
