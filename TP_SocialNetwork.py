# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:14:29 2019

@author: SERHIR Mohamed
"""

l_arcs = [('Andreas', 'Bernard'), ('Bernard', 'Andreas'), ('Cathie', 'Andreas'), ('Cathie', 'Daniel'), ('Bernard', 'Cathie'), ('Bernard', 'Daniel'), ('Bernard', 'Emmanuel'), ('Daniel', 'Emmanuel')]

#print(l_arcs)

# 1. function gr
"""
    dictionnary = {}
    print("ICI")
    for arc in l_arcs:
        print(arc)
        print(arc[1])
        if arc[0] not in dictionnary.keys():
            dictionnary[arc[0]] = arc[1]
        else:
            dictionnary[arc[0]] = arc[1]
    for arc in l_arcs:
        if arc[1] not in dictionnary.values():
            dictionnary[arc[0]] = arc[1]
"""

def gr(l_arcs):
    gr = {}
    for orig, extr in l_arcs:
        if orig in gr:
            gr[orig].append(extr)
        else:
            gr[orig] = [extr]
        if extr not in gr:
            gr[extr] = []
            
    return gr

print("gr: ", gr(l_arcs))

# 2. function ens_sommets (l_arcs) 

def ens_sommets(l_arcs):
    sommets = set()
    for orig, extr in l_arcs:
        sommets.add(orig)
        sommets.add(extr)
            
    return sommets

print("ens_sommets: ", ens_sommets(l_arcs))

# 3.function ens_influenced (l_arcs, n) 

def ens_influenced(l_arcs, n):
    return set([extr for orig, extr in l_arcs if orig == n])

print("ens_influenced: ", ens_influenced(l_arcs, 'Daniel'))
    
# 4. ens_influencing (l_arcs, n) 

def ens_influencing(l_arcs, n):
    return set([orig for orig, extr in l_arcs if extr == n])

print("ens_influencing: ", ens_influencing(l_arcs, 'Daniel'))


# 5. function Isolated(l_arcs) the set of people who have no influence on any other people.

def isolated(l_arcs):
    origines = set()
    extremites = set()
    
    for orig, extr in l_arcs:
        origines.add(orig)
        extremites.add(extr)
    return extremites - origines

print("Isolated: ", isolated(l_arcs))

# 6. function sources(l_arcs) the set of people that are not influenced by others

def sources(l_arcs):
    origines = set()
    extremites = set()
    
    for orig, extr in l_arcs:
        origines.add(orig)
        extremites.add(extr)
    return (origines - extremites)

print("sources: ", sources(l_arcs))
    