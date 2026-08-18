words_list = input().split()                     # let's make our input into the string
diction = {}                                     # we need empty dict in first

for word in words_list:                          # loop which working with all items from list  
    diction[word] = diction.get(word, 0) + 1     # putting 'word' in dict, always plusing '1' at index

for word, count in diction.items():              # word is a key, count is a meaning ow key
    print(word, count)                         

