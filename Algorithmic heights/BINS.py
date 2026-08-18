def binary_search(array, target):                                # this fumction gibe us logarithmic speed O(logN)
    low = 0                                                      # first index of array
    high = len(array) - 1                                        # remember that len starts with '1'
    
    while low <= high:                                           # main loop of binary search
        mid = (low + high) // 2                                  # find middle position
        
        if array[mid] == target:                                 # if we found target in first step...
            return mid + 1                                       # remember that we need start index '1'
        elif array[mid] < target:                                # if our target at the right corner
            low = mid + 1                                        # we increase 'low' so much which optimise memory and steps
        else:                                                    # if our target at the left corned
            high = mid - 1                                       # so here we decrease 'high' in the half!
            
    return -1                                                    # give out '-1' if target not found


with open('rosalind_bins.txt', 'r', encoding='utf-8') as file:   # read our file
    expected_count_dict = int(file.readline().strip())           # len of sorted stream
    expected_count_chaos = int(file.readline().strip())          # len of chaos stream

    first_stream = list(map(int, file.readline().split()))       # sorted stream
    second_stream = list(map(int, file.readline().split()))      # chaos stream


expected_chaos = []                                              # make our check-list
for chaos_number in second_stream:                               # loop whick take all numbers for chaos step by step
    result_index = binary_search(first_stream, chaos_number)     # very fast search chaos number in sorted array
    expected_chaos.append(result_index)                          # full our check-list with results of searching

print(*(expected_chaos))                                         # print all results on one line