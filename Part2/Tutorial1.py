# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 08:36:25 2019

@author: SERHIR Mohamed
"""

# Exercie 1
# 1. Variable

x = 2
y = 'Pierre'

print(x, y)

print('type of', x, ': ', type(x), 'and type of', y, ': ', type(y))

x = 'Marie'
print('type of', x, ': ', x)

# 2. Lists, Sets, Dictionaries
"""
• List is a collection which is ordered and changeable. Allows duplicate members.
• Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
• Set is a collection which is unordered and unindexed. No duplicate members.
• Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""

# 3. Conditions and loops
print('\n3. Conditions and loops')

a = 2
b = 10

if b > a:
    print('b greater than a')
else:
    print('b is not greater than a')

for i in range(a + 1):
    print(i * i)

# 4 Functions
"""
A function is a block of code which only runs when it is called. You can pass data, known as
parameters, into a function. A function can return data as a result.
"""


# 5. Problem 1
def timeConversion():
    print('Please enter a hour in this format: hh:mm:ssPM or hh:mm:ssAM')
    s = input()
    if s[8:10] == 'AM':
        if int(s[0:2]) > 12:
            print('Your hour is not valid: ' + s[0:2])
        elif 59 < int(s[3:5]) < 0:
            print('Your minute is not valid: ' + s[3:5])
        elif 59 < int(s[6:8]) < 0:
            print('Your sec is not valid: ' + s[6:8])
        else:
            s = s[0:8]
    elif s[8:10] == 'PM':
        if 12 > int(s[0:2]) > 24:
            print('Your hour is not valid: ' + s[0:2])
        if 59 < int(s[3:5]) < 0:
            print('Your minute is not valid: ' + s[3:5])
        elif 59 < int(s[6:8]) < 0:
            print('Your sec is not valid: ' + s[6:8])
        else:
            s = str((int(s[0:2]) + 12)) + s[2:8]
    else:
        print('Please enter a correct value')
    return s


#print('Result: ' + timeConversion())

# 6. Problem 2
""" Given two numbers A and B. Iterate from the smallest to the biggest number and print the sum
of the current number and previous number at each iteration. At the end, print the sum of all the
intermediate calculated numbers.
Example :
Input : A=2, B=4
 Print 3 ; 2+1
 Print 5; 3+2
 Print 7
 End : Print 15
Tips :
• range and sum functions"""
print('\n Problem 2')

a = 2
b = 4
listN = []

if a > b:
    smallest = b
    biggest = a
elif b > a:
    smallest = a
    biggest = b
else:
    print('The numbers are equals...')
    smallest = a
    biggest = b

for i in range(smallest, biggest +1):
    print(i)
    if i == smallest:
        listN.append(smallest + smallest - 1)
        """
    else:
        listN.append(listN[i] + listN[i] - 1)
        """
    print(listN[i])


print(sum(listN) - (a+b))

# 7. Problem 3
print('\nProblem 3:')
