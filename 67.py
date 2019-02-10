a=int(input())
for i in range(1,11):
	if a%10==0:
		break
	elif a%10==1:
		a=a+9

	elif a%10==2:
		a=a+8

	elif a%10==3:
		a=a+7
	
	elif a%10==4:
		a=a+6
	elif a%10==5:
		a=a+5
	
	elif a%10==6:
		a=a+4
	elif a%10==7:
		a=a+3

	elif a%10==8:
		a=a+2
	
	elif a%10==9:
		a=a+1
print(a)

