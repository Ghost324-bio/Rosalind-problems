def get_fibonacci_by_index(n):                   # build function which always increase 'a' and 'b'
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a                                     # not 'yield!!!' cause we need only one number at end

user_index = int(input("Введите индекс: "))      # we dont need '+1' here cause we using first and second Fib numbers
if user_index < 0:
    print('Введён неправильный индекс')
else:
    print(get_fibonacci_by_index(user_index))