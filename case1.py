def sum_and_count_positive(arr):
    sum_pos = 0
    count_pos = 0
    
    for i in arr:
        if i > 0:
            sum_pos += i
            count_pos += 1
    
    return sum_pos, count_pos


# Тесты

# пустой
N = []
total_sum_pos, total_count_pos = sum_and_count_positive(N)
print(f"Сумма положительных элементов: {total_sum_pos}")
print(f"Количество положительных элементов: {total_count_pos}")
print("***********************")

# все -
N = [-1, -2.5, -3]
total_sum_pos, total_count_pos = sum_and_count_positive(N)
print(f"Сумма положительных элементов: {total_sum_pos}")
print(f"Количество положительных элементов: {total_count_pos}")
print("***********************")

# все +
N = [2, 3, 1.5]
total_sum_pos, total_count_pos = sum_and_count_positive(N)
print(f"Сумма положительных элементов: {total_sum_pos}")
print(f"Количество положительных элементов: {total_count_pos}")
print("***********************")

# c 0
N = [0, -1, 0, -2]
total_sum_pos, total_count_pos = sum_and_count_positive(N)
print(f"Сумма положительных элементов: {total_sum_pos}")
print(f"Количество положительных элементов: {total_count_pos}")
print("***********************")

# cмешанные
N = [-1, 2, 0, 4]
total_sum_pos, total_count_pos = sum_and_count_positive(N)
print(f"Сумма положительных элементов: {total_sum_pos}")
print(f"Количество положительных элементов: {total_count_pos}")
print("***********************")