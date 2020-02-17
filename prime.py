user=int(input('enter no. '))
for i in range(2,user//2+1):
	if user%i==0:
		print(user,'is not prime number')
		break
else:
	print(user,'is prime number')
