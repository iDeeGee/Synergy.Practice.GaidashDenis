def sum_and_count_positive(arr):
    """Функция подсчёта суммы и кол-ва полож.элементов."""
    sum_pos = 0
    count_pos = 0
    
    for i in arr:
        if i > 0:
            sum_pos += i
            count_pos += 1
    
    return sum_pos, count_pos


def input_array():
    """Функция ввода элементов пользователем."""
    while True:
        try:
            user_input = input("Введите элементы массива через пробел: ")
            
            # замена ,
            user_input = user_input.replace(",", ".")
            
            # Каст значения в список float
            arr = [float(x) for x in user_input.split()]
            return arr
        except ValueError:
            print("Ошибка! Введите число или дробь.\n")


if __name__ == "__main__":
    Result = input_array()
    total_sum_pos, count_pos = sum_and_count_positive(Result)
    print(f"Сумма положительных элементов: {total_sum_pos}")
    print(f"Количество положительных элементов: {count_pos}")