import sys                                               # it's important to optimise data flow and memory

def dna_coding_rna_decoder(stream_dna):                  # if you have coding DNA and need only replace 'T' to 'U'
    for line in stream_dna:                              # read our flow step by step
        yield line.replace('T', 'U').replace('t', 'u')   # give out new line by C optimised algorithm (.replace)

def dna_template_rna_decoder(stream_dna):                # so if we have not-coding DNA and need full complement result
    trans_matrix = str.maketrans('ATCGatcg', 'UAGCuagc') # make complement matrix for several replacing
    for line in stream_dna:                              # make loop for step by step replacing
        yield line.translate(trans_matrix)               # give out results: data flow went through translate matrix

stream_dna = sys.stdin                                   # lazy optimised read object from console

chosen_decoder = dna_coding_rna_decoder(stream_dna)      # SWITCH MODE HERE, RENAME FUNCTION DEPENDS ON TYPE OF DNA

for transformed_nucl in chosen_decoder:                  # read loop with actual data and chosen function
    sys.stdout.write(transformed_nucl)                   # and give out our result with very fast algorithm
    
sys.stdout.flush()                                       # reset buffer