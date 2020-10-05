"""
This function asks the user for their credit card number and tells them whether or not it is valid.
"""



def ask_user():
    string = (input("Please input your credit card number\n"))
    numbers = list(map(int, string))
    if card_length(numbers):
        validation(numbers)
    else:
        print("The credit card number you entered is invalid")


"""
This function takes the credit card number as a parameter and checks the length of the credit card number 
to see if it is valid or not.
"""


def card_length(num):
    length = len(num)
    if 13 <= length <= 16:
        if num[0] == 4 or num[0] == 5 or num[0] == 6 or (num[0] == 3 and num[1] == 7):
            return True
    else:
        return False


"""
This method takes the list of numbers and tells the user if it is a valid combination with a print statement
"""


def validation(numbers):
    odd_results = odd_digits(numbers)
    even_results = even_digits(numbers)
    sum_of_results = odd_results + even_results
    if sum_of_results % 10 == 0:
        print("This credit card number is valid")
    else:
        print("This credit card number is invalid")


"""
This function takes the credit card number as a string list parameter and adds all
of the even digits in it.
"""


def even_digits(numbers):
    sum_even = 0
    even_digits = numbers[-2::-2]                                 #because it is a list of integers, the slice notation is different
    for i in range(0, len(even_digits)):                          #this line iterates over the sliced list
        number = even_digits[i] * 2                               #this line multiplies the even placed digits by 2
        if number > 9:                                            #if the number is greater than 9
            str_number = str(number)                              #this line converts the integer back to a string, so that we can add up the 2 digit number
            number = (eval(str_number[0]) + eval(str_number[1]))  #this line adds the 2 digit number
        sum_even += number
    return sum_even



"""
This function takes the credit card number as a string list parameter and adds all
of the odd digits in it.
"""


def odd_digits(numbers):
    sum_odd = 0
    odd_digits = numbers[-1:0:-2]                                 #because it is a list of integers, the slice notation is different
    for i in range(0, len(odd_digits)):                           #this line iterates over the sliced list
        sum_odd = sum_odd + odd_digits[i]                         #this line adds the numbers in the odd places
    return sum_odd


"""
This is the main function that defines our first function called ask_user
"""


def main():
    ask_user()


"""
This calls the main function
"""
if __name__ == '__main__':
    main()
