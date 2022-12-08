def temp():
	choice = int(input('Press 1 to convert celsius to fahrenheit\nPress 2 to convert fahrenheit to celsius.\n'))
	if choice == 1:
		cel = float(input('Enter temperature in celsius\n'))
		print((cel*1.8)+32,' deg fahrenheit')
	elif choice == 2:
		fah = float(input('Enter temperature in fahrenheit\n'))
		print((fah - 32)*(5/9),' deg celsius')
	else:
		print('Invalid value entered')

def currency():
	# We can use dictionary to store units and multiply the 'to' to the value in dict
	holder = {'Rupees':[1,0.012,1.65,0.012,0.76],
			  'Dollar':[81.79,1,135.27,0.95,62.30],
			  'Yen':[0.60,0.0074,1,0.0070,0.46],
			  'Euro':[86.38,1.06,142.89,1,66.30],
			  'Ruble':[1.31,0.016,2.17,0.015,1]
	}
	print('Choose currency to be converted')
	count = 0
	#attach index to every key
	for k,v in holder.items():
		print(f'\t{count} ',k)
		count += 1
	#take currencies which need to be converted as int
	while True:
		try:
			frm = int(input('From (int)\t'))
			to = int(input('To (int)\t'))
			break
		except:
			print('You entered wrong format')
	#retrieve name from holder 
	a = list(holder)[frm]
	b = list(holder)[to]
	multiplier = list(holder.values())[frm][to]
	
	money_user_have = int(input(f"How many {a} do you have?\t"))

	exch = money_user_have * multiplier
	print(f'{money_user_have} {a} = {exch} {b}')

















def opener():
	x = int(input('Welcome to unit convertor\nWhat do you want to convert\n1. Temperature\n2. Currency\n'))
	if x == 1:
		temp()
	elif x == 2:
		currency()



if __name__ == '__main__':
	opener()
