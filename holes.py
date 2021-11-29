# Let us assume paper as the plane and a letter as a curve on the plane, then each letter divides the plane into regions. For
# example letters "A", "D", "O", "P", "R" divide the plane into two regions so we say these letters each have one hole.
# Similarly, letter "B" has two holes and letters such as "C", "E", "F", "K" have no holes. We say that the number of holes in
# the text is equal to the total number of holes in the letters of the text. Write a program to determine how many holes are in a
# given text.

l1 = ['A', 'D', 'O', 'P', 'R', 'Q']
l2 = ['B']
l3 = [
    'C', 'E', 'F', 'K', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z'
]
str = input("Enter the text: ")
str = str.upper()
count = 0
for i in str:
    if i in l1:
        count += 1
    elif i in l2:
        count += 2
    elif i in l3:
        count += 0
print("The number of holes in the text is: ", count)
