"""
Given a positive integer 'x' (with even number of digits in it), compute the difference between the sum of the digits occurring in the alternate positions (starting from the first position) and the sum of the digits occurring in the alternate positions, starting from the last rightmost position of 'x'.
"""


def reverse(n):
    rev = 0
    while (n != 0):
        rev = (rev * 10) + (n % 10)
        n //= 10
    return rev


def getSum(n):
    n = reverse(n)
    sumOdd = 0
    sumEven = 0
    c = 1
    while (n != 0):
        if (c % 2 == 0):
            sumEven += n % 10
        else:
            sumOdd += n % 10
        n //= 10
        c += 1
    print("Odd :", sumOdd)
    print("Even :", sumEven)
    print("Difference :", sumOdd - sumEven)


x = int(input("Enter a number : "))
getSum(x)

# Enter a number : 142536
# Odd : 6
# Even : 15
# Difference : -9