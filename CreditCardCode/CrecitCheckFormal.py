#def main():
CreditCardNum = (str(input("give your creditcard number with spaces ")))
num = list(map(int, CreditCardNum.split()))
print(num)


def length_card(num):
    if num >= 13 and num <= 16:
        if num [0] == "4" or num [0] == "5" or num [0] == "6" or (num [0] == "3" and num [1] == "7"):
            return True
    else:
        return False


def even_digits(num):
    length = len(num)
    sum = 0
    for i in range(length-2,-1,-2):
        number = eval(num[i])
        number = number * 2
        if number > 9:
            strNumber = str(number)
            number = eval(strNumber[0] + eval(strNumber[1]))
            sum += number
        return sum

def odd_digits(num):
    length = len(num)
    SumOdd = 0
    for i in range(length-1, -1, -2):
        num += SumOdd
    return SumOdd
