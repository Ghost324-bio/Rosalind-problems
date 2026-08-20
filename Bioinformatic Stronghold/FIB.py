"""
This algoryth count Fibonacci numbers with parallel assignment
Demonstratiom of rabbit problem
Script works with any months and productivity of rabbits
"""

def fib_counter(months, litter_size):
    # parameters of first month
    adults = 0
    youngsters = 1
    
    # loop for rest months (not including first = '-1')
    for _ in range(months - 1):
        # count new assignment at every month and update
        adults, youngsters = adults + youngsters, adults * litter_size
        
    # give out result when loop ended
    return adults + youngsters

if __name__ == "__main__":
    # input month count and productivity in one line
    n, k = map(int, input().split())
    result = fib_counter(n, k)
    print(result)