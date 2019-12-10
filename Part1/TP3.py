# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:52:32 2019

@author: SERHIR Mohamed
"""

"""
TP Python 3

Given different scored marks of students. We need to find grades. The test score is an average of the respective marks scored in assignments, tests and lab-works. The final test score is assigned using below formula.
10 % of marks scored from submission of Assignments
60 % of marks scored from Test
30 % of marks scored in Lab-Works
 Grade will be calculated according to :
1. score >= 90 : "A"
2. score >= 80 : "B"
3. score >= 70 : "C"
4. score >= 60 : "D"
A- Display students’ averages and grades.
B- Calculate the total class average and letter grade of class.
C- Use the Bubble sort to display student average.
"""

# 1. Using Lists, write a program that creates a Stack along with the necessary functions to Pop, Push and Display its content.

myStack = []
stackSize = 3
def DisplayStack():
 print("Stack currently contains:")
 for Item in myStack:
  print(Item)
  
def Push(Value):
 print('Try to push', Value)
 if len(myStack) < stackSize:
  myStack.append(Value)
 else:
  print("Can't push: stack is full!")
  
def Pop():
 print('Try to pop')
 if len(myStack) > 0:
  myStack.pop()
 else:
  print("Can't pop: stack is empty.")
  
Push('A')
Push('B')
print(myStack.top())
Push('C')
DisplayStack()

input("Press any key when ready...")
Push('D')
DisplayStack()
input("Press any key when ready...")
Pop()
DisplayStack()
input("Press any key when ready...")
Pop()
Pop()
DisplayStack()

#2. Write a program that uses Bubble Sort to sort a list of values.

