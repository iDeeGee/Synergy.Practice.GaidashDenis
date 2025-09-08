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
    """Функция ввода данных пользователем."""
    while True:
        try:
            N = int(input("Введите размерность массива: "))
            if N <= 0:
                print("Размерность должна быть положительной!\n")
                continue
            break
        except ValueError:
            print("Ошибка! Введите целое число для размерности!.\n")
    
    while True:
        try:
            N_elements = input("Введите элементы массива через пробел: ")
            
            # замена ,
            N_elements  = N_elements .replace(",", ".")
            
            # Каст в список float
            arr = [float(x) for x in N_elements.split()]
            return arr
        except ValueError:
            print("Ошибка! Введите число или дробь.\n")


if __name__ == "__main__":
    A = input_array()
    total_sum_pos, count_pos = sum_and_count_positive(A)
    print(f"Сумма положительных элементов: {total_sum_pos}")
    print(f"Количество положительных элементов: {count_pos}")