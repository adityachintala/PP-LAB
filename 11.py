# Experiment 11
# Say you have the boring task of finding every phone number and email address in a long web page or document. Write a program to search for the phone numbers and email addresses from a given text fileand store them in a separate text file.

# Program :

file = open('text.txt', 'r')
file1 = open('phone.txt', 'w')
file2 = open('email.txt', 'w')
text = file.read().split()
file.close()
print(text)
for i in text:
    if '@' in i:
        file2.write(i + '\n')
    elif len(i) == 10:
        file1.write(i + '\n')
file1.close()
file2.close()