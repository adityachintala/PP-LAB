"""
Write a program to check whether the given number is Consecutive Four Sum Number or not. Consecutive Four Sum  Number: A positive integer is called as a `Consecutive Four Sum (CFS) number' if that number can be expressed as the sum of four consecutive positive integers.
"""


def cfsn(n):
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if j == i + 1:
                for k in range(j + 1, n + 1):
                    if k == j + 1:
                        for l in range(k + 1, n + 1):
                            if l == k + 1:
                                if i + j + k + l == n:
                                    print(i, j, k, l)


n = int(input("Enter a number : "))
cfsn(n)

# Enter a number : 10
# 1 2 3 4
