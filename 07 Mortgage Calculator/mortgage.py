print('Enter the details of loan you want?')
p = int(input('principal = '))
r = int(input('Rate of simple interest(%) = '))
t = int(input('Time period(yrs) = '))

interest = p*(r/100)*t
print(f'Interest to be returned = {interest}')
amt = interest + p
number_of_m = 12 * t
emi_month = amt/number_of_m
print(f'You can pay Rs.{emi_month} every month')