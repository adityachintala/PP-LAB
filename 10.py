# Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print
# number // 2 and return this value. If number is odd, then collatz() should printand return 3 * number + 1. Then write a
# program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the
# value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you‘ll
# arrive at 1! Even mathematicians aren‘t sure why. Your program is exploring what‘s called the Collatz sequence,
# sometimes called ―the simplest impossible math problem.‖)
# The input and output of this program could look something like this:
# Input=
# Enter number: 3
# Output=
# 10 5 16 8 4 2 1


def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


try:
    n = int(input('Enter a number: '))
    while n != 1:
        n = collatz(n)
        print(n, end=' ')
except ValueError:
    print('Please enter a valid INTEGER')