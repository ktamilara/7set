num1=input()
a=0
l=['a','e','i','o','u','A','E','I','O','U']
for x in num1:
	if x in l:
		a=a+1
		break
if(a>0):
	print('yes')
else:
	print('no')
