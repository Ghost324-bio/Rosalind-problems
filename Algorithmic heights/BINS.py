# 1. Функция классического бинарного поиска
def binary_search(array, target):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if array[mid] == target:
            return mid + 1  # Rosalind требует индексацию с 1
        elif array[mid] < target:
            low = mid + 1   # Искомое число справа
        else:
            high = mid - 1  # Искомое число слева
            
    return -1  # Если число не найдено


# 2. Чтение файла (ваш исходный блок)
with open('rosalind_bins.txt', 'r', encoding='utf-8') as file:
    expected_count_dict = int(file.readline().strip())       # Длина отсортированного массива
    expected_count_chaos = int(file.readline().strip())      # Длина хаотичного массива

    first_stream = list(map(int, file.readline().split()))   # Отсортированный массив
    second_stream = list(map(int, file.readline().split()))  # Хаотичный массив (запросы)


# 3. Поиск без использования словаря
expected_chaos = []
for chaos_number in second_stream:
    # Вместо expected_dict.get() вызываем функцию бинарного поиска
    result_index = binary_search(first_stream, chaos_number)
    expected_chaos.append(result_index)


# 4. Вывод результата в одну строку
print(*(expected_chaos))
