seq1 = 'agcgccttgaattcggcaccaggcaaatctcaaggagaagttccggggagaaggtgaagac'
seq2 = 'cggggagcggggagccgagccgcaagacgagcgagcggactgcccaccacgagcgacaacz'
s = len(seq1)
print(s)
l = ("n" in seq2)
print(l)
nb_a = seq1.count('a')
p = (nb_a / s) * 100
print(p)
EcoRI = 'GAATTC'
BamHI = 'GGATCC'
p1 = seq1.count(EcoRI)
print(p1)
p2 = seq2.count(BamHI)
print(p2)
EcoRI = str.lower(EcoRI)
print(EcoRI)
p1 = seq1.count(EcoRI)
print(p1)
j = 0
for j in range(0, s, 3):
    gc2 = seq1[j:j + 3]
    print(gc2)


def compter_acides_nucleiques(adn):
    nombre_occurrences = {"a": 0, "c": 0, "g": 0, "t": 0}
    for acide_nucleique in adn:
        nombre_occurrences[acide_nucleique] += 1
    return nombre_occurrences


dna = "tgctacgcattaggcgcctgagctagctcctactacggtgaccttgatcgactggatcgacgagacgtcgctagctagtacgcgacgatctgcgtaggctacgtacagttcgcgatacgtgccgactcagg"
compteur = compter_acides_nucleiques(dna)
for acide_nucleique in compteur:
    print((acide_nucleique, compteur[acide_nucleique]))
    #print(nombre_occurrences[acide_nucleique] * 100 / len(dna))
