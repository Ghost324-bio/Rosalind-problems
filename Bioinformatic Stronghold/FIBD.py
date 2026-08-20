"""
This algorithm counts Mortal Fibonacci Numbers with a custom productivity parameter
Simulates rabbits that live for 'm' months and produce 'k' pairs of children each month
"""

def generic_mortal_fib_counter(months, lifespan, litter_size):
    # initialize the lifespan track with list
    rabbits = [0] * lifespan
    rabbits[0] = 1  # one pair of newborns

    for _ in range(months - 1):
        # sum all adults and multiply by productivity
        newborns = sum(rabbits[1:]) * litter_size

        # age the population and remove the dead ones
        rabbits.pop()
        rabbits.insert(0, newborns)

    return sum(rabbits)


if __name__ == "__main__":
    # example input: months (n), lifespan (m), productivity (k)
    n, m, k = map(int, input().split())
    result = generic_mortal_fib_counter(n, m, k)
    print(result)

"""
How it works? For example, months = 6, lifespan = 3, productivity = 1
Initial state (Month 1): [1, 0, 0]  <- 1 newborn pair starts here
Inside the loop (Passage of time):
- 2nd month: newborns = 0 -> pop oldest (0) -> insert(0, 0) -> [0, 1, 0]
- 3rd month: newborns = 1 -> pop oldest (0) -> insert(0, 1) -> [1, 0, 1]
- 4th month: newborns = 1 -> pop oldest (1) -> insert(0, 1) -> [1, 1, 0]
- 5th month: newborns = 1 -> pop oldest (0) -> insert(0, 1) -> [1, 1, 1]
- 6th month: newborns = 2 -> pop oldest (1) -> insert(o, 2) -> [2, 1, 1]
End of loop: total sum = 2 + 1 + 1 = 4
"""
