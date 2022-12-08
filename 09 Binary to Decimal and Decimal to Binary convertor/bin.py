# Binary to Decimal and Back Converter - 
# Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.

class BaseConvertor:
	def __init__(self):
		choice = int(input('Choose one: \n1. Binary to Decimal conversion\n2. Decimal to Binary conversion\n'))
		if choice == 1:
			self.bin_dec()
		elif choice == 2:
			self.dec_bin()
		else:
			print('Incorrect choice entered')

	def bin_dec(self):
		# Binary to decimal equivalent
		bin = int(input('Enter Binary number with base 2: '))	#1011001
		counter = 0
		total = 0

		while bin>1:
			r = int(bin%10)
			bin = bin/10
			if r==1:	
				total = total + 2**counter
			counter = counter+1

		print('Decimal equivalent is ',total)

	def dec_bin(self):
		#Decimal to binary
		dec = int(input('/nEnter Decimal value of base 10: '))	#13
		b = ''
		while dec > 1:
			r = int(dec%2)
			dec = dec/2
			b += str(r)
		print('Binary equivalent is ',b[::-1])

one = BaseConvertor()
