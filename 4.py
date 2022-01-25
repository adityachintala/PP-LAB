# Given a positive integer 'x' (with even number of digits in it), compute the difference between the sum of the
# digits occurring in the alternate positions (starting from the first position) and the sum of the digits occurring in the
# alternate positions, starting from the last rightmost position of 'x'.

n = input("Enter number : ")
if len(n) % 2 != 0 or int(n) <= 0:
    print("Invalid")
else:
    s1, s2 = 0, 0
    for i in range(0, len(n), 2):
        s1 += int(n[i])
        s2 += int(n[i + 1])
    print(abs(s1 - s2))
