a, b = map(int, input().split()) #we have problem to sum all odd numbers between 'a' and 'b'
sum_final = 0                    #start sum

if a % 2 == 0:                   #what we need to do if 'a' even number?
    a += 1                       #let's transform 'a' to odd number

for i in range(a, b + 1, 2):     #optimise our code with 'for'
    sum_final += i

print(sum_final)                 #you can double-check reult with your calculator if you unsure :)