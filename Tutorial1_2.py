"""
Created on Sat Dec  7 10:36:32 2019

@author: SERHIR Mohamed
"""


def isInList(listNumbers, number):
    for x in listNumbers:
        if number == x:
            return True
    return False


number = 2
listNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Is the number ', number, 'in the list ? ', isInList(listNumbers, number))
