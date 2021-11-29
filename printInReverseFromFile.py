# Write a program to print each line of a file in reverse order. Also compute the number of characters, words and lines in a file.

file = open("adty.txt", "r")
lines = file.readlines()
file.close()
for line in lines:
    print(line[::-1])
file = open("adty.txt", "r")
lines = file.readlines()
file.close()
words = 0
characters = 0
for line in lines:
    words += len(line.split())
    characters += len(line)
print("Words =", words)
print("Characters =", characters)
print("Number of lines =", len(lines))