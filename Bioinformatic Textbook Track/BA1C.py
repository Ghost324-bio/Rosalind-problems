import sys

def dna_complement(stream_dna):
    trans_matrix = str.maketrans('ATCG', 'TAGC') # Rosalind input is strictly uppercase
    
    for line in stream_dna:
        # Strip the trailing newline so it doesn't get reversed into the data
        clean_line = line.rstrip('\r\n')
        if clean_line:
            # Translate and reverse the clean sequence block
            yield clean_line.translate(trans_matrix)[::-1]

if __name__ == "__main__":
    stream_dna = sys.stdin
    
    # We collect the reversed blocks. To reverse the GLOBAL stream correctly, 
    # we need to print them from last to first if the input had multiple lines.
    # However, Rosalind BA1C provides the entire DNA on a SINGLE line.
    
    for transformed_nucl in dna_complement(stream_dna):
        sys.stdout.write(transformed_nucl)
        
    # Print a single clean newline at the very end of the entire stream
    sys.stdout.write('\n')
    sys.stdout.flush()