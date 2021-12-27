# Write a program to check whether the given number is Consecutive Four Sum Number or not. Consecutive Four Sum
# Number: A positive integer is called as a `Consecutive Four Sum (CFS) number' if that number can be expressed as
# the sum of four consecutive positive integers.

n = int(input("Enter number : "))
for i in range(1, n // 2):
    if i * 4 + 6 == n:
        print("CFS")
        break
else:
    print("Not CFS")