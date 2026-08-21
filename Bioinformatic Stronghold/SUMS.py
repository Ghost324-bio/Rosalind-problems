"""
This script solves the SUBS problem (Finding a Motif in DNA)
It runs in O(N * M) time complexity and maintains O(N) memory overhead
'N' means DNA length, 'M' means motif length
"""

import sys
from itertools import batched

def dna_reader():
    # streams non-empty lines from standard input
    for line in sys.stdin:
        line = line.strip()
        if line:
            yield line

# stream configuration
lines_stream = dna_reader()

# batched packs the text into pairs: (dna, motif)
for pair in batched(lines_stream, 2):
    dna, motif = pair
    motif_len = len(motif)
    
    # we use a sliding index window instead of heavy suffixes to keep memory low
    for index in range(len(dna)):
        if dna[index : index + motif_len] == motif:
            # our case requires 1-based indexing
            print(index + 1, end=' ')
    print() # new line for the next potential pair

"""
Some insights (shortly building upon the HAMM case):
1. 'sys.stdin' is always waiting for new data, and 'batched' (which works from Python 3.12+) yields lines in pairs here.
2. It helps to maintain a minimal (constant) memory footprint and flush variables for every new data flow.
3. Remember that 'batched' expects an even number of lines to complete the pair.
   Unlike FASTA, the entire DNA stream needs to be placed on a single line to correctly locate the motif.
4. Something new for me — using a "Sliding window" to search for specific sequences in a DNA stream (not just single nucleotides).
5. It works like analyzing a dynamically changing DNA segment, where the start and end positions depend on the 'index' value in the loop.
6. It feels like working with a tiny silk stream as a seamstress, instead of a butcher's chopping step-by-step that overheats the memory :)
7. Why is print() at the end? We create a new line for the output to easily separate and compare different data flows.
"""
