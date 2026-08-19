import sys                                               # let's read DNA object from console

def dna_complement(stream_dna):                          # main function
    trans_matrix = str.maketrans('ATCGatcg', 'TAGCtagc') # complement matrix
    for line in stream_dna:                              # loop which reading data flow step by step
        yield line.translate(trans_matrix)[::-1]         # 'C' optimised translating data AND giving native reverse!

stream_dna = sys.stdin                                   # lazy optimised read object from console

for transformed_nucl in dna_complement(stream_dna):      # read loop with actual data
    sys.stdout.write(transformed_nucl)                   # and give out our result with very fast algorithm
    
sys.stdout.flush()                                       # reset buffer