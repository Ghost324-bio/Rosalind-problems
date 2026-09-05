"""
This script solves PROT case (transform RNA string to protein)
It takes O(1) memory and O(N) time, N - number of RNA strings
Script safe for errors and report you if data is 'unclean'
"""

import sys

# our prepared codon dict
rna_codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop', 'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

# this function releases RNA lazy reading and validate data flow 
def rna_stream():
    valid_nucleotides = {'A', 'U', 'G', 'C'}   # our validation set
    for line in sys.stdin:
        line = line.strip().upper()
        if not line:
            continue

        # transform our data flow to set
        line_consist = set(line)
        if not line_consist.issubset(valid_nucleotides): 
            # obviously RNA flow includes only four nucleotides
            # but if set has trash symbols - give 'sys.stderr' flag and report for user why it wasn't proceed
            print(f'Unsorted data at RNA flow "{line}". Please clean this line.', file=sys.stderr)
            continue

        yield line

def rna_to_protein(stream):
    # unpack our generator and transform it to string
    for rna_string in stream:
        protein_chain = []   # make empty list for future protein
        rna_length = len(rna_string)   # now we can calculate length of RNA
        
        # read our line with sliding window with codon size (3)
        for index in range(0, rna_length, 3):
            # if we have less than 3 symbols - give 'sys.stderr' flag and report for user about unreadable part
            if rna_length - index < 3:
                print(f'The end of RNA flow "{rna_string[index:]}" is not a codon.', file=sys.stderr)
                break
                
            # here we realise our sliding codon window
            codon = rna_string[index : index + 3]
            amino_acid = rna_codon_table.get(codon)
            
            # stop protein constructing if we meet stop-codon
            if amino_acid == 'Stop':
                break

            # when 'amino_acid" variable not empty - let's put it into our prepared list    
            if amino_acid:
                protein_chain.append(amino_acid)
                
        # transform our list to one huge string
        yield "".join(protein_chain)

# initialise pipeline
if __name__ == "__main__":
    print("Enter the RNA flow for translating to protein (Ctrl+D for exit):")
    raw_stream = rna_stream()
    results_stream = rna_to_protein(raw_stream)
    
    for result in results_stream:
        print(f"Protein: {result}")

"""
How it works?
1. Script has two defs with separate functions, which helps to make pipelines
2. Some new - '.issubset', which helps to validate clean data (need to write validation key)
3. Second function prepared to react when 'Codon sliding window' meets 'Stop' and when RNA string has less than 3 symbols
4. Pipeline works with every new line while you won't close console
"""