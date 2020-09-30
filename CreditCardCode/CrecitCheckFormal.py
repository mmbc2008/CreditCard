"""
This function asks the user for their credit card number and tells them whether or not it is valid.
"""


def ask_user():
    string = (str(input("Please input your credit card number\n")))
    numbers = list(map(int, string.split()))
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
        if num[0] == "4" or num[0] == "5" or num[0] == "6" or (num[0] == "3" and num[1] == "7"):
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


def even_digits(num):
    length = len(num)
    total = 0
    for i in range(length - 2, -1, -2):
        number = eval(num[i])
        number = number * 2
        if number > 9:
            strNumber = str(number)
            number = eval(strNumber[0] + eval(strNumber[1]))
            total += number
        return total


"""
This function takes the credit card number as a string list parameter and adds all
of the odd digits in it.
"""


def odd_digits(num):
    length = len(num)
    sumOdd = 0
    for i in range(length - 1, -1, -2):
        num += sumOdd
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
