def hap(num):
	temp = 0
	while num > 0:
		r = num % 10
		num = num//10
		r = r*r
		temp = temp + r
	if temp > 9:
		hap(temp)
	else:
		if temp == 1:
			print('Happy Number')
		else:
			print('Unhappy number')

hap(int(input('Enter a number\t')))