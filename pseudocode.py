The purpose of this program is to detect whether a provided number is a valid credit card number.

credit_card_number = ask user for input of the digits #the digits should be between 13 and 16.

#step one from assignment
reverse credit_card_number
FOR every second  digit from credit_card_number:
   number1 = digit times two
   IF number1 is greater than nine:
      number1 = add the two digits
	  return number1
   ELSE: 
      return number1
print number1

#step two from assignment
number2 = add every digit retrieved from number1
print number2

#step three from assignment
FOR every digit in odd place:
    number3 = number3 + the digit in odd place
	return number3
print number3

#step four from assignment
number4 = number2 + number3

#step five from assignment
IF number4 / 10 = integer:
   print credit card number is valid
ELSE:
   print credit card number is invalid
  