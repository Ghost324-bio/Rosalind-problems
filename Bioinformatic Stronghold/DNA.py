dna_struc = {'A': 0, 'C': 0, 'G': 0, 'T': 0}                            # dict with four DNA nucleotides 

user_dna = input()                                                      # user give variable DNA structure

for nucl in user_dna:                                                   # make loop which check symbols step by step in input
    if nucl in dna_struc:
        dna_struc[nucl] += 1                                            # if we found our nucleotide = increase our count

print(dna_struc['A'], dna_struc['C'], dna_struc['G'], dna_struc['T'])   # print on one line