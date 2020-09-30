credit_card_number = input("enter your credit card number>>")
digits = [int(digit) for digit in str(credit_card_number)] #x are the individual numbers
digits.reverse()
print(digits) #to check if the previous step went okay

#step 1 from assignment
added_numbers = 0
evendigits = digits[1::2]
print(evendigits)  #to check if the previous step went okay
for digit in evendigits:
    number1 = digit*2
    number1 = sum(int(digit) for digit in str(number1))
    #step 2
    added_numbers = added_numbers+number1
print(added_numbers) #to check if the step went correctly

#step 3 from assignment
odd_digits = digits[::2]
number2 = sum(odd_digits)
print(number2) #to check if the step went correctly


#step 4 from assignment
total_numbers = number2 + added_numbers
print(total_numbers)

if total_numbers % 10 == 0:
    print('This is a valid credit card number')
else:
    print('this is not a valid credit card number')











