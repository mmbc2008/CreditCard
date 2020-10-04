"""
This function asks the user for their credit card number and tells them whether or not it is valid.
"""


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


def even_digits(numbers):
    total = 0
    even_digits = numbers[-2::-2]        #because it is a list of integers, the slice notation is different
    for i in range(0, len(even_digits)): #this line iterates over the sliced list
        number = even_digits[i] * 2      #this line multiplies the even placed digits by 2
        if number > 9:               #if the number is greater than 9
            str_number = str(number)  #this line converts the integer back to a string, so that we can add up the 2 digit number
            number = (eval(str_number[0]) + eval(str_number[1]))  #this line adds the 2 digit number
        total += number
    return total



"""
This function takes the credit card number as a string list parameter and adds all
of the odd digits in it.
"""


def odd_digits(numbers):
    sumOdd = 0
    odd_digits = numbers[-1:0:-2]        #because it is a list of integers, the slice notation is different
    for i in range(0, len(odd_digits)):  #this line iterates over the sliced list
        sumOdd = sumOdd + odd_digits[i]  #this line adds the numbers in the odd places
    print("This is the odd sum " + str(sumOdd))
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
