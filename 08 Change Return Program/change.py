#Change Return Program** - The user enters a cost and then the amount of money given.
#The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

money = {1:0,2:0,5:0,10:0,20:0,50:0,100:0,200:0,500:0,2000:0}

bill = int(input('Enter total bill amount to be paid: '))
rec = int(input('Enter amount recieved : '))
res =dict(reversed(list(money.items())))

if (rec - bill)>0:
	due = rec - bill
	print('Total amount returned = ',due)
	while due>0:
		#This for loop checks the denominations which needs to be given  
		for d in res: 
			if d <= due:	# Should we give this note d
				due = due-d				
				# increment the value of d in money //// add one more note of this denomination
				money[d] = money[d] + 1

elif(rec-bill)==0:
	print('Thankyou visit again')
else:
	print('Pay Rs.',bill-rec)


# This loop checks the number of notes of every denomination from dictionary and prints to the user where notes are more than 0.
for x in money:
	if money[x] > 0:
		print(f'{money[x]} notes of Rs.{x}')
