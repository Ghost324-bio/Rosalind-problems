import sys                                                            # we need to write optimised code for DNA count 
from Bio.Seq import Seq                                               # besides 'pure' Python, let's use Bio.Seq tool

def count_nucleotides_lazy_biopython(stream_dna, chunk_size=65536):   # function with main DNA flow and size of read
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}                         # base dict where we save our DNA counts
    
    while True:                                                       # loop working while we have symbols for read
        raw_chunk = stream_dna.read(chunk_size)                       # read raw symbols (about 64KB memory needed)
        if not raw_chunk:                                             # stops strictly when stream is completely empty
            break
            
        chunk = raw_chunk.rstrip('\r\n')                              # safe remove trailing newlines after empty check
        if not chunk:                                                 # if the chunk contained only newlines, skip counting
            continue
            
        dna_seq = Seq(chunk)                                          # transform our reading data to 'bio object'
        counts["A"] += dna_seq.count("A")                             # use our dict count for A
        counts["C"] += dna_seq.count("C")                             # use our dict count for C
        counts["G"] += dna_seq.count("G")                             # use our dict count for G
        counts["T"] += dna_seq.count("T")                             # use our dict count for T
        
    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}" # give out results of counting

if __name__ == "__main__":                                            # it means code working only like main programm
    stream_dna = sys.stdin                                            # catch DNA object from console
    result = count_nucleotides_lazy_biopython(stream_dna)             # use our function for data flow
    
    sys.stdout.write(result + "\n")                                   # catch results from function and lazy print it
    sys.stdout.flush()                                                # reset buffer

