"""
This function asks the user for their credit card number and tells them whether or not it is valid.
"""
import re


def ask_user():
    string = (input("Please input your credit card number\n"))
    numbers = list(map(int, string))
    print(numbers)
    if card_length(numbers):
        validation(numbers)
    else:
        print("The credit card number you entered is invalid")


"""
This function takes the credit card number as a parameter and checks the length of the credit card number 
to see if it is valid or not.
"""


def card_length(num):
    print("Does it get here")
    length = len(num)
    print(length)
    if 13 <= length <= 16:
        print("Does it get here too")
        if num[0] == 4 or num[0] == 5 or num[0] == 6 or (num[0] == 3 and num[1] == 7):
            print("Is it true")
            return True
    else:
        print("Is it false")
        return False


"""
This method takes the list of numbers and tells the user if it is a valid combination with a print statement
"""


def validation(numbers):
    print(numbers)
    odd_results = odd_digits(numbers)
    print("This is the odd result " + str(odd_results))
    even_results = even_digits(numbers)
    print("This is the even result " + str(even_results))
    sum_of_results = odd_results + even_results
    if sum_of_results % 10 == 0:
        print("This credit card number is valid")
    else:
        print("This credit card number is invalid")


"""
This function takes the credit card number as a string list parameter and adds all
of the even digits in it.
"""


def even_digits(num):
    length = len(num)
    total = 0
    second_to_last = length - 2
    for i in range(second_to_last, -1, -2):
        number = num[i]
        number = number * 2
        if number > 9:
            strNumber = str(number)
            number = eval(strNumber[0] + eval(strNumber[1]))
            total += number
        return total
    print("This is the total"+str(total))

"""
This function takes the credit card number as a string list parameter and adds all
of the odd digits in it.
"""


def odd_digits(num):
    length = len(num)
    end = length - 1
    sumOdd = 0
    for i in range(-2, end, -1):
        num += sumOdd
    print("This is the odd sum "+str(sumOdd))
    return sumOdd


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
