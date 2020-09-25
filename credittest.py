creditcard = input("enter your creditcard number>>")
digits = [int(x) for x in str(creditcard)] #x are the individual numbers
digits.reverse()
print(digits)

added_numbs = 0
evendigits = digits[1::2]
print(evendigits)
for x in evendigits:
    mult_numb = x*2
    mult_numb = sum(int(digit) for digit in str(mult_numb))
    added_numbs = added_numbs+mult_numb
print(added_numbs)


odd_digits = digits[::2]
print(odd_digits)

total_number = sum(odd_digits) + added_numbs
print(total_number)

if total_number % 10 == 0:
    print('This is a valid creditcard number')
else:
    print('this is not a valid creditcard number')











