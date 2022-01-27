# Write a program to print each line of a file in reverse order. Also compute the number of characters, words and lines in a file.

file = open("sample.txt", "r")
lines = file.readlines()
file.close()
print('Reverse order:')
for line in lines[::-1]:
    print(line, end='\n')
w = 0
c = 0
for line in lines:
    w += len(line.split())
    c += len(line) - line.count('\n')
print("Number of lines:", len(lines))
print("Number of words:", w)
print("Number of characters:", c)