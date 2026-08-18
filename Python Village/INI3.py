phrase = input()                       #let's see we have huge unsorted text and dataset for slice it
a, b, c, d = map(int, input().split()) #also use map() for working with several numbers

phrase1 = phrase[a:b + 1]               #remember, the ending index of slice is exclusive
phrase2 = phrase[c:d + 1]               #that's why we need write '+1' here

print(phrase1, end=' ')                #I wanted to print my slices in one line using 'end'
print(phrase2)                         #you can try it with any phrase input and indexes