def adder(c1,c2):
	result = c1+c2
	return result

def subtract(c1,c2):
	result = c1-c2
	return result

def multiply(c1,c2):
	result = c1 * c2
	return result

def division(c1,c2):
	result = c1 / c2

def start():
	print('Enter complex numbers')
	try:
		c1 = complex(input('Enter C1 without whitespace = \t'))
		c2 = complex(input('Enter C2 without whitespace = \t'))
	except:
		print('Enter without spaces')
		return

	operation = input('Select operation + - * /\t')
	if operation == '+':
		result = adder(c1,c2)
		print("Sum is \t",result)
	elif operation == '-':
		result = subtract(c1,c2)
		print("subtraction is \t",result)
	elif operation == '*':
		result = multiply(c1,c2)
		print("multiply is \t",result)
	elif operation == '/':
		result = division(c1,c2)
		print('division is \t',result)
	else:
		print('Incorrect operation')
start()