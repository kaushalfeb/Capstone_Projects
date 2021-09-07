from decimal import Decimal,getcontext

def fact(n):
	temp = Decimal(1)
	for x in range(1,n+1):
		temp *= x
	return temp

def cal(n):
	temp = Decimal(0)
	getcontext().prec = n+1
	for x in range(100+n):
		temp += Decimal(1)/Decimal(fact(x))
	return temp

def main():
	val = int(input("\tHow many values do you wish after decimal :\t"))
	y = cal(val)
	print("\n\te :",y)

if __name__ == "__main__":
	main()