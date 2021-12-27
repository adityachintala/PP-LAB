# Given a number A which contains only digits 0's and 1's. Your task is to make all digits same by just flipping
# one digit (i.e. 0 to 1 or 1 to 0) only. If it is possible to make all the digits same by just flippingone digit
# then print 'YES' else print 'NO'.

n = input("Enter number : ")
l = len(n)
c1, c2 = 0, 0
for i in range(l):
    if n[i] == '0':
        c1 += 1
    else:
        c2 += 1
if c1 == l - 1 or c2 == l - 1:
    print("YES")
else:
    print("NO")