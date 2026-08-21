"""
This script counts Hamming distance = value of mutations in pair of DNA strings
It takes O(1) memory and O(N) time difficulty
"""

import sys
from itertools import batched

def dna_reader():
    # main function which reads lines and give out data if line ends
    for line in sys.stdin:
        line = line.strip()
        if line:
            yield line

# here is string generator
lines_stream = dna_reader()

# batched takes two elements from data flow and transform it in tuple (dna1, dna2)
for pair in batched(lines_stream, 2):
    dna1, dna2 = pair
    
    # generator expression for counting number of mutations
    count_mut = sum(n1 != n2 for n1, n2 in zip(dna1, dna2))

    # print our Hamming distance
    print(count_mut)

"""
Some tips:
1. 'batched' works from Python 3.12+
2. 'sys.stdin' is always waiting for new data, but 'batched' always yields new results right after two lines.
3. If we end our data stream with an odd number of lines (or the file includes an odd number), we'll get a ValueError 
   because 'batched' is strictly expecting two elements for unpacking.
4. The 'pair' tuple stores only references to the string objects, not the strings themselves; 
   that's why the tuple won't cause memory overhead even with massive strings and will maintain a constant size.
5. On the next iteration, the loop with 'batched' assigns new values to dna1 and dna2, allowing Python's 
   garbage collector to purge the old unreferenced data and instantly free up memory.
"""