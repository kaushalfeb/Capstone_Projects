# Calculator - A simple calculator to do basic operators. Make it a scientific calculator for added complexity.

def calc(a,b,op):
	if op == '+':
		print(a+b)
	elif op == '-':
		print(a-b)
	elif op == '/':
		try:
			print(a/b)
		except:
			print('Division by zero')
	elif op == '*':
		print(a*b)
	else:
		print('Oops')

def main():
	a = int(input('Enter a value\t'))
	b = int(input('Enter b value\t'))
	op = input('Enter operation + - / *\t')

	calc(a,b,op)

if __name__ == '__main__':
	main()
