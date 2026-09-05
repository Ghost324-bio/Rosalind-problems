"""
This script solves the BA1B problem (Find the Most Frequent K-mers in a String)
It features structured stream pairing via 'batched' and local memory flushing,
ensuring controlled memory overhead and O(N * k) time complexity.
"""

import sys
from itertools import batched
from collections import Counter

def dna_reader():
    # streams non-empty lines from standard input
    for line in sys.stdin:
        line = line.strip()
        if line:
            yield line

# stream configuration
lines_stream = dna_reader()

# batched handles input data in pairs: (dna string, k value)
for pair in batched(lines_stream, 2):
    dna, k_str = pair
    k = int(k_str)
    
    # a local smart dictionary that flushes automatically at the end of the loop iteration
    kmer_counter = Counter()
    
    # sliding index window moves down the DNA ribbon like a seamstress with a magnifying glass
    for index in range(len(dna) - k + 1):
        kmer = dna[index : index + k]
        kmer_counter[kmer] += 1
        
    if kmer_counter:
        # accessing the internal list/tuple matrix to grab the highest count value
        max_count = kmer_counter.most_common(1)[0][1]
        
        # dynamic dict unpacking via .items() to print all top leaders sharing the record
        for kmer, count in kmer_counter.items():
            if count == max_count:
                print(kmer, end=' ')
        print() # resetting the console line for the next data stream segment

"""
Architectural Insights:
1. True code reusability: This script scales up the robust stream design built for SUBS,
   proving that good architectural patterns adapt effortlessly to new logic.
2. Memory safety buffer: While storing k-mers scales with DNA length inside the iteration, 
   the 'batched' pipeline destroys the Counter dictionary immediately after the print statement, 
   ensuring the application never hoards data across thousands of sequences.
3. Fast execution layer: Using Python's C-optimized 'Counter.most_common' and '.items()' unpacking
   bypasses slower, high-level loops, allowing the code to analyze strings at native execution speeds.
4. How 'most_common' works?
   it takes most common elements from dict by this algorith:
   - (1)... - how much we need leaders of dict? At this case - only first
   - After that we're getting tupple in list: [(kmer, count)]
   - (...)[0]... - it helps take our tupple from list - (kmer, count)
   - (...)[...][1] - it helps take the nu,ber of counts and assign it to our variable
"""

