from random import randint
out = ['Head','Tail']
repeat = int(input('How many tosses to perform?'))
head = 0 
tail =0
for a in range(0,repeat):
	x = randint(0,1)
	print(out[x])
	if x:
		head = head+1
	else:
		tail = tail+1
print(f'Heads were {head}, tails were {tail}')

