"""
This function asks the user for their credit card number and tells them whether or not it is valid.
"""


def ask_user():
    # Takes the credit card number entered by the user and stores it in the variable credit card no
    credit_card_no = (input("Please input your credit card number\n"))
    # Converts the credit card no into a list of integers
    numbers = list(map(int, credit_card_no))
    # calls the validation function if the card_length function returns true
    if card_length(numbers):
        validation(numbers)
    else:
        print("The credit card number you entered is invalid")


"""
This function takes the credit card number as a parameter and checks the length of the credit card number 
to see if it is valid or not.
"""


def card_length(num):
    # Calculating the length of the numbers list
    length = len(num)
    # If the length of the list is between 13 and 16
    if 13 <= length <= 16:
        # This makes sure that the beginning of the card number is valid
        if num[0] == 4 or num[0] == 5 or num[0] == 6 or (num[0] == 3 and num[1] == 7):
            return True
    else:
        return False


"""
This method takes the list of numbers and tells the user if it is a valid combination with a print statement
"""


def validation(numbers):
    # Stores the sum of the odd indices added up
    odd_results = odd_digits(numbers)
    # Stores the sum of the even indices added up
    even_results = even_digits(numbers)
    # Adds the even and odd sum up
    sum_of_results = odd_results + even_results
    # Takes the modulus of the total sum by 10
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
    # As this is a list of integers, the slice notation is different
    even_numbers = numbers[-2::-2]
    # This line iterates over the sliced list
    for i in range(0, len(even_numbers)):
        # In this line multiplies the even placed digits by 2
        number = even_numbers[i] * 2
        # If the number is greater than 9
        if number > 9:
            # This converts the integer back to a string, so that we can add up the 2 digit number
            str_number = str(number)
            # In this line adds the 2 digit number
            number = (eval(str_number[0]) + eval(str_number[1]))
            # Here all the even numbers are added up
        sum_even += number
        # Returns the final sum value
    return sum_even


"""
This function takes the credit card number as a string list parameter and adds all
of the odd digits in it.
"""


def odd_digits(numbers):
    sum_odd = 0
    # Due to the fact that it is a list of integers, the slice notation is different
    odd_numbers = numbers[-1:0:-2]
    # This line iterates over the sliced list
    for i in range(0, len(odd_numbers)):
        # Here the numbers in odd places are summed up
        sum_odd = sum_odd + odd_numbers[i]
        # Returns the final sum value
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
