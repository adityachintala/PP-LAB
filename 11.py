# Experiment 11
# Say you have the boring task of finding every phone number and email address in a long web page or document. Write a program to search for the phone numbers and email addresses from a given text fileand store them in a separate text file.

# Program :

import re

file = open('text.txt', 'r')
file1 = open('phone.txt', 'w')
file2 = open('email.txt', 'w')
text = file.read().split()
file.close()
for i in text:
    if all(c.isdigit() for c in i):
        file1.write(i + '\n')
    if re.match(r'[\w\.-]+@[\w\.-]+', i):
        file2.write(i + '\n')
file1.close()
file2.close()
print('Done')