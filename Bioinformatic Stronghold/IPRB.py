""""
This script solving IPRB case (First Mendel's law)
Here we are calculating probability of dominant sign in next generation
It takes O(1) memory and O(N) time, N - times of calculus
"""

import sys

def data_stream():
    # this function release lazy reading of infinite data flow 
    for line in sys.stdin:
        if not line.strip():   #reader skip empty lines and don't proceed it 
            continue
        try:
            yield map(int, line.split())    # reader give out all numbers with spaces
        except ValueError:
            print(f"Error: wrong input '{line.strip()}'", file=sys.stderr)

def calculate_probability(stream):
    # this function release probability's calculus of dominant sign  
    for k, m, n in stream:
        t = k + m + n
        var_t = t * (t - 1)
        
        # safe mode if population don't have more than one parent
        if var_t <= 0:
            yield 0.0
            continue
            
        p_nn = (n * (n - 1)) / var_t
        p_mn = (m * n) / var_t
        p_mm = (0.25 * m * (m - 1)) / var_t
        
        p_rec = p_nn + p_mn + p_mm
        yield round(1 - p_rec, 5)

# Initialise of Pipeline
if __name__ == "__main__":
    print("Enter k, m, n with spaces (Ctrl+D for exit):")
    raw_stream = data_stream()
    results_stream = calculate_probability(raw_stream)
    
    for result in results_stream:
        print(f"Dominant probability: {result:.5f}")

""""
How it works?
1. Here I made isolated two functions which work in one pipeline
2. 'data_stream" optimised for numbers and can report about data issue (for example, if we have strings, not int)
3. After this report script won't crush and continue to proceed other lines
4. If you want to calculate recesive probability, just edit 'yield' in calculated function and text in pipeline
5. Also you can change round of final probability if you need it (35 and 44 lines)
"""
