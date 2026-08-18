import sys                                                     # so in this problem we sorting infinite stream of text for even lines
import itertools                                               # with this we can operato data flow without overheatin memory

def main():
    with open("rosalind_ini5.txt", "r", encoding="utf-8") as file_stream:
        even_lines = itertools.islice(file_stream, 1, None, 2) # lazy data flow, skip first line(1), don't stop(None) and use even (2)
    
        for line in even_lines:
            sys.stdout.write(line)                           # lazy print
            sys.stdout.flush()                               # clean the output buffer

if __name__ == "__main__":                                   #without this our function won't starts
    main()
