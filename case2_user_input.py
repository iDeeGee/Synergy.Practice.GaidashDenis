def count_and_product_greater(arr, B):
    """Функиция для поиска больше B и их произведение."""
    count = 0
    product = 1
    for i in arr:
        if i > B:
            count += 1
            product *= i
    return count, product if count > 0 else 0


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
            print("Ошибка! Введите целое число.\n")
    
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


def input_number_b():
    """Функция ввода B от пользователя."""
    while True:
        try:
            B = float(input("Введите число B: "))
            return B
        except ValueError:
            print("Ошибка! Нужно ввести число.\n")


if __name__ == "__main__":
    A = input_array()
    B = input_number_b()
    count, product = count_and_product_greater(A, B)
    print(f"\nКоличество элементов больше B ({B}): {count}")
    print(f"Их произведение: {product}")