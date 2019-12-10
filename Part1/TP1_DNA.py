# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

DNA1 = 'agcgccttgaattcggcaccaggcaaatctcaaggagaagttccggggagaaggtgaagattagggttt'
DNA2 = 'cggggagtggggagttgagtcgcaagatgagcgagcggatgtccactatgagcgataataagt'

# Display the length of each DNA chain.
print("\n# Display the length of each DNA chain.\n")
lenDNA1 = len(DNA1)
lenDNA2 = len(DNA2)

print("Lenght of: \n DNA1 : ", lenDNA1, "\n DNA2 : ", lenDNA2)

#	Display the bigger DNA length.
print("\n# Display the bigger DNA length.\n")
if lenDNA1 > lenDNA2:
    print("Bigger DNA lenght: ", lenDNA1, " is: ", DNA1)
else:
    print("Bigger DNA lenght: ", lenDNA2, " is: ", DNA2)
    
#	Find out how many base “n” contains each DNA
print("\n#	Find out how many base “n” contains each DNA\n")

print("DNA1 contains: ", DNA1.count("n"), " numbers of n")
print("DNA2 contains: ", DNA2.count("n"), " numbers of n")

#	Find out how many base “a” contains each DNA
print("\n#	Find out how many base “a” contains each DNA\n")
print("DNA1 contains: ", DNA1.count("a"), " numbers of a")
print("DNA2 contains: ", DNA2.count("a"), " numbers of a")

#	Find the percentage of each base in each string.
print("\n#	Find the percentage of each base in each string.\n")
      
print("Percentage of base a for DNA 1", round(DNA1.count('a') / lenDNA1 * 100, 2), "%" )
print("Percentage of base c for DNA 1", round(DNA1.count('c') / lenDNA1 * 100, 2), "%" )
print("Percentage of base g for DNA 1", round(DNA1.count('g') / lenDNA1 * 100, 2), "%" )
print("Percentage of base t for DNA 1", round(DNA1.count('t') / lenDNA1 * 100, 2), "%" )
print("\n")
print("Percentage of base a for DNA 2", round(DNA2.count('a') / lenDNA2 * 100, 2), "%" )
print("Percentage of base c for DNA 2", round(DNA2.count('c') / lenDNA2 * 100, 2), "%" )
print("Percentage of base g for DNA 2", round(DNA2.count('g') / lenDNA2 * 100, 2), "%" )
print("Percentage of base t for DNA 2", round(DNA2.count('t') / lenDNA2 * 100, 2), "%" )
      
#	Display the Genetic codes included in each DNA (a genetic code is a sequence of three bases). 
print("\n#	Display the Genetic codes included in each DNA\n")

print("DNA1: \n")
if lenDNA1 % 3 == 0:
    for i in range (0,  lenDNA1, 3):
        print(DNA1[i:i + 3])
else:
    print("False DNA1");

print("DNA2: \n")
if lenDNA2 % 3 == 0:
    for i in range (0,  lenDNA2, 3):
        print(DNA2[i:i + 3])
else:
    print("False DNA2");

#	Given that EcoRI = ’GAATTC’ and BamHI = ’GGATCC’ are two patterns; verify if the aforementioned DNAs contain these patterns.
print("\n#	Given that EcoRI = ’GAATTC’ and BamHI = ’GGATCC’ are two patterns\n")
      
EcoRI = 'GAATTC'
BamHI = 'GGATCC'

if EcoRI.lower() in DNA1:
    print("ok")
else:
    print("no ok")
if BamHI.lower() in DNA1:
    print("ok")
else:
    print("no ok")
    
if EcoRI.lower() in DNA2:
    print("ok")
else:
    print("no ok")
if BamHI.lower() in DNA2:
    print("ok")
else:
    print("no ok")
    
#	Calculate the number of occurrences of each base in each chain
print("\n#	Calculate the number of occurrences of each base in each chain\n")

print("Number of occurences of EcoRI in DNA1 : ", DNA1.count(EcoRI.lower()) )
print("Number of occurences of BamHI in DNA1 : ", DNA1.count(BamHI.lower()) )
 
print("Number of occurences of EcoRI in DNA2 : ", DNA2.count(EcoRI.lower()) )
print("Number of occurences of BamHI in DNA2 : ", DNA2.count(BamHI.lower()) )


#	Calculate the percentage of each base in the sequence.
print("\n#	Calculate the percentage of each base in the sequence.\n")
      
#	function count_nucleic_acids (dna) 
print("\n#  function count_nucleic_acids (dna) \n")
      
def count_nucleic_acids(DNA):
    nbOccurrences = {"a": 0, "c": 0, "g": 0, "t": 0}

    for acide_nucleique in DNA:
        nbOccurrences[acide_nucleique] += 1

    return nbOccurrences

 

dna ="tgctacgcattaggcgcctgagctagctcctactacggtgaccttgatcgactggatcgacgagacgtcgctagctagtacgcgacgatctgcgtaggctacgtacagttcgcgatacgtgccgactcagg"

compteur = count_nucleic_acids(dna)

for acide_nucleique in compteur:

    print((acide_nucleique, compteur[acide_nucleique]))

    print( ((compteur["c"] + compteur["g"]) * 100 / len(dna) ))
