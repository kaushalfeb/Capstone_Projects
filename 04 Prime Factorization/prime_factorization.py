def prime(interval):
	primes = []
	for number in range(2,interval):
	    flag = True
	    for x in range(2,number):
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
	domain = int(input("Enter a value to show its prime factorization: "))
	x = prime(domain)
	# x is a list of all prime numbers upto (but not including) domain
	
	i=0
	print("Prime factorization is ",end=" = ")
	# we run the loop upto the number of elements in list x.
	total = len(x)
	final = []
	for a in range(total):
		while True:
			if domain % x[a] == 0:
				final.append(x[a])
				domain /= x[a] 
			else:
				break


if __name__ == '__main__':
	main()