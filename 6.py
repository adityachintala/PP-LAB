# Write a program to create a list of tuples from given list having number and its cube in each tuple.

nums = input("Enter numbers : ")
nums = list(map(int, nums.split()))
l = []
for i in nums:
    l.append((i, i**3))
print(l)
