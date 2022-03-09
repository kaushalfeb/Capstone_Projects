def prf():
    n = int(input("Enter the value whose prime factors should be displayed "))
    i = 2
    print(n,end = ' = ')
    while(i<=n):
        if n%i == 0:
            print(i,end = ' ')
            n = n/i
        else:
            i +=1
def main():
	prf()
if __name__ == '__main__':
	main()