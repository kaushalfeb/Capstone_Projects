"""
Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
"""

def prime(fro,to):
	'''user tells from which index to start printing primes'''
	primes = []
	for number in range(fro,to):
	    flag = True
	    for x in range(fro,number):
	        if x<number:
	            if number%x != 0:
	                x+=1
	            else:
	                flag = False
	        else:
	            break
	    if flag:
	        primes.append(number)
	return primes

def main():
	i=2 # start prime numbers from i index

	while True:
		user = input("Do you wish to view next prime number?\t Y/N\n")
		try:
			'''
			if user presses Y call prime function by inserting index value and print result
			'''
			if user == 'Y' or user == 'y':
				pass
		except:
			'''
			 if user enters wrong character prompt to insert Y or N
			'''


if __name__ == '__main__':
	main()