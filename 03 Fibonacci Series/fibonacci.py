def cal(n):
	a = 0
	b = 1
	c = 0
	fib = []
	for x in range(n):
		a = b 
		b = c
		c = b + a
		fib.append(b)
	print('\n',fib)

def main():
	t = int(input('How long fib series do you want\t'))
	cal(t)

if __name__ == '__main__':
	main()