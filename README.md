This is the project from group 47:

For our assignment we had to make a program based on Luhn's algorithm that can detect
whether a provided number is a valid credit card number following these set of rules:

1. Double every second digit from right to left:

        a. If doubling of a digit results in a two-digit number add up the two digits to get a
        single-digit number.
2. Add all single-digit numbers from Step 1.
3. Add all digits in the odd places from right to left in the card number.
4. Sum the results from Step 2 and Step 3.
5. If the result in Step 4 is divisible by 10, the card number is correct. Otherwise, the
number is invalid.

We were allowed to make our own assumptions of what is permitted, but we have to assume that the
computer will generate numbers randomly or that a user will be entering a number of only a few
digits. If the provided input is not permitted, how will our algorithm handle such cases? We specify
this in a second, more sophisticated version of our algorithm.

This image links to the presentation of our project:
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/ViTDjae7hmA/0.jpg)](https://youtu.be/ViTDjae7hmA)
