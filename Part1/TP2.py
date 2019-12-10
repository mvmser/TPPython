# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:30:33 2019

@author: SERHIR Mohamed
"""

#1. Function displayTitle(content, width) -  display content centered

def displayTitle(content, width):
    #First verify the max word size
    for x in content:
        if len(x) >= width:
            width = len(x) + 2
        #print(len(x))
        #print(width)
    
    #Generate header and footer
    header = ""
    for y in range(width + 4):
        header += "*"       
    footer = header
    
    print(header)
    
    for line in content:
        print("*",line.center(width),"*")
        
    print(footer)


#displayTitle(["The number of DNA bases", "is huge", "", "However, not all bases are used to transmit genetic fea"], 20)

#With a fileText
def displayTitle(textFile, width):
    #First verify the max word size
    for line in open(textFile).readlines():
        print (line)
        if len(line) >= width:
            width = len(line) + 2
    #Generate header and footer
    header = ""
    for y in range(width + 4):
        header += "*"       
    footer = header
    
    #print
    print(header)
    
    for line in open(textFile).read().splitlines():
        print("*",line.center(width),"*")
    
    print(footer)
    
#displayTitle("title.txt", 2)


#2. COmpare content of 2 txtes files if same then true

def isSameContent(content1, content2):
    a = open(content1).read()
    b = open(content2).read()
    
    if a == b:
        return True
    return False

#print(isSameContent("Content1.txt", "Content2.txt"))

#3. Moving average

def movingAverage(S1, n):
    averages = []
    print("S1: ", S1)
    for i in range(0, len(S1)):
        if(i <= len(S1) - n):
           averages.append(round(sum(S1[i:i+n]) / n, 2)) 
           #print(S1[i:i+n])
    return averages

S1 = [2,3,5,7,11,13,17]
print("S2: ", movingAverage(S1, 3))


#4. Two main function computeMeanAndStdDev, testRandom
import math
import random

def computeMeanAndStdDev(n):
    somme = 0.0
    sommeCarres = 0.0
    
    for i in range(n):
        x = random.random()
        somme = somme + x
        sommeCarres = sommeCarres + x * x
        moyenne = somme / n
        ecartType = math.sqrt((sommeCarres / n) - moyenne * moyenne)
    return moyenne, ecartType
    print(moyenne, ecartType)
        
        
def testRandom(n):
    moyenne, ecartType = computeMeanAndStdDev(n)
    print("moyenne", moyenne, "erreur", abs(moyenne - 0.5))
    print("ecartType:", ecartType, "erreur", abs(ecartType - math.sqrt(1/12)))

print(testRandom(100))
computeMeanAndStdDev(10)