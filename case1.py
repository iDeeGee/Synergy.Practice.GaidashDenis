def sum_and_count_positive(arr):
    sum_pos = 0
    count_pos = 0
    
    for i in arr:
        if i > 0:
            sum_pos += i
            count_pos += 1
    
    return sum_pos, count_pos

# Пример 
# if __name__ == "__main__":
A = [1, -3, 5, 0, 7, -2]
total_sum_pos, count_pos = sum_and_count_positive(A)
print(f"Сумма положительных элементов: {total_sum_pos}")
print(f"Количество положительных элементов: {count_pos}")

