# Write a program to create a list of tuples from given list having number and its cube in each tuple.

list = [1, 2, 3, 4, 5]
list2 = []
tuple = ()
for i in list:
    tuple = (i, i**3)
    list2.append(tuple)
print(list2)


# [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]