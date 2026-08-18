with open('rosalind_bins.txt', 'r', encoding='utf-8') as file:   # open our database

    expected_count_dict = int(file.readline().strip())           # we have safe index for first massive
    expected_count_chaos = int(file.readline().strip())          # we have safe index for second massive

    first_stream = list(map(int, file.readline().split()))       # we have one huge line with spaces between numbers
    second_stream = list(map(int, file.readline().split()))      # use map, imcluding 'int', spaces and list transform

expected_dict = {}                                               # make our dict for based massive
for index, number in enumerate(first_stream, start=1):           # remember that we need start index = 1
    expected_dict[number] = index                                # append 'number' like key and his meaning like 'index'

if len(first_stream) != expected_count_dict:
    print(f"Ошибка! Ожидалось {expected_count_dict} чисел, а прочитано {len(first_stream)}")

expected_chaos = []                                              # make our check-list
for chaos_number in second_stream:                               # take all numbers in 'chaos_number' step by step
    result_index = expected_dict.get(chaos_number, -1)           # check if we have this number in based dict
    expected_chaos.append(result_index)                          # write result of check in our check-list

if len(expected_chaos) != expected_count_chaos:
    print(f"Ошибка! Ожидалось {expected_count_chaos} чисел, а прочитано {len(expected_chaos)}")

print(*(expected_chaos))                                         # all results in one line with spaces