credit_card_number = input("enter your credit card number>>")
digits = [int(digit) for digit in str(credit_card_number)]
digits.reverse()
print("this is the reversed input ", digits) #to check if the step went correctly

#step 1 from assignment
added_numbers = 0
even_digits = digits[1::2]
print('this is the list of even digits from the input ', even_digits)  #to check if the previous step went okay
for digit in even_digits:
    number1 = digit*2
    number1 = sum(int(digit) for digit in str(number1))
    #step 2
    added_numbers = added_numbers+number1
print('these are the added values of step 2: ', added_numbers) #to check if the step went correctly

#step 3 from assignment
odd_digits = digits[::2]
print('this is the list of odd digits from the input ',odd_digits) #to check if the step went correctly
number2 = sum(odd_digits)
print('these are the added values of all odd digits: ', number2) #to check if the step went correctly


#step 4 from assignment
total_numbers = number2 + added_numbers
print('this is the sum of the odd and the even digits: ', total_numbers) #to check if the step went correctly

if total_numbers % 10 == 0:
    print('This is a valid credit card number')
else:
    print('this is not a valid credit card number')











