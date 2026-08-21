"""
This optimised FASTA parser has O(1) difficulty for memory and O(N) for time
Loop has coordinated operation between switching recording of different variables (ID, actual seq flow)
"""

import sys

def parse_fasta_stream():
    current_id = None
    current_seq_parts = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        if line.startswith('>'):
            if current_id:
                # tip: "".join here transforming our list to huge string
                yield current_id, "".join(current_seq_parts)
            current_id = line[1:]
            current_seq_parts = []
        else:
            current_seq_parts.append(line)

    # when loop ends and we don't meet any '>', function give out last parameters
    if current_id:
        yield current_id, "".join(current_seq_parts)

"""
How it works?
1. Safe mode for the first reading: when parser meets '>' at the first time, we don't have actual ID (none)
That's why function doesn't give out any data and starts with reading
2. If line starts with '>', we update ID and don't touch seq parts.
3. If line doesn't have '>', we update list of seq parts.
4. When we meet '>' at the second and rest times, function give out current ID and seq list
5. You can switch the type of saving data at the pointed place
"""

# MAIN SWITCH MODE: Here we catching ID and dna flow from function

best_id = ""
max_gc_content = -1.0   # safe parameter: if FASTA doesn't have any DNA parts, it'll show '-1'

# 'current_id' becomes 'fasta_id', 'current_seq_parts' becomes 'dna'
for fasta_id, dna in parse_fasta_stream():
    
    # interesting step: now our DNA data is not a list, but a huge string, that's why we can easy count nucleotides
    gc_count = dna.count('C') + dna.count('G')
    total_count = len(dna)
    
    if total_count > 0:
        gc_content = (gc_count / total_count) * 100
        
        # check if we break maximum of 'CG' count
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            best_id = fasta_id

# print our result with round
print(best_id)
print(f"{max_gc_content:.6f}")

"""
How works our outer counter?
1. loop always catching new data from yield
2. After catching it counting 'CG' content and counting percents of it (%)
3. If our loop variable bigger than outer max_content — make assignment for count and id
4. At the next steps it always compare with new data at assign if it needs
5. When yield stops give to loop new data, script prints final result
"""