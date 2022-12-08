'''Calculating the Luhn algorithm by hand includes a few different steps. They include the following.

      1. Write down the credit card number:

4417 1234 5678 9113

      2. Starting from the first number, double every other digit.

4(x2) 4 1(x2) 7 1(x2) 2 3(x2) 4 5(x2) 6 7(x2) 8 9(x2) 1 1(x2) 3

The doubled numbers result in: 8 2 2 6 10 14 18 2

        3. If the result of the doubling ends up with a two digits, then add those two digits together:

10 = 1+0 14= 1+4 18= 1+8

        4. Add up all numbers: 8+4+2+7 + 2+2+6+4 + 1+0+6+1+4+8 + 1+8+1+2+3 = 70

If the final sum is divisible by 10, then the credit card is valid. 
If it is not divisible by 10, the number is invalid or fake. 
In the above example, credit card number 4417 1234 5678 9113 has passed the Luhn test.
'''
def remove(string):
      return string.replace(" ","")

def credit_card_validator():
      card= input('Enter credit card number:\t')
      try:
            card_number = int(remove(card))
            if len(str(card_number)) != 16:
                  raise exception
                  print("Digits entered",len(str(card_number))) 
      except:
            print('Invalid Card Number')
      else:
            num = card_number
            count = 1
            temp = 0
            adder = 0 
            while num>1:
                  r = int(num%10)
                  num = num/10
                  temp = temp*10 + r

            while temp>1:
                  r = int(temp%10)
                  temp = temp/10

                  if count == 1:
                        count = 0
                        r = r*2
                        if r>9:
                              rem = int(r%10)
                              r = rem+1
                        
                  elif count == 0:
                        count = 1
                        
                  adder = adder + r
            r = adder%10 
            if r == 0: 
                  print('Card is Valid')
            else:
                  print('Card is Invalid')

            print("Sum is ",adder)
credit_card_validator()