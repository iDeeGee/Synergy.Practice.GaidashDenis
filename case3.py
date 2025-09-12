# Код доступен на github: https://github.com/iDeeGee/Synergy.Practice.GaidashDenis/blob/main/case3.py
import random
import time
import threading

stop_flag = False  # Флаг для остановки генерации

def input_thread():
    """Функция для отслеживания ввода 0 от пользователя"""
    global stop_flag
    while True:
        user_input = input()
        if user_input.strip() == "0":
            stop_flag = True
            break

def generate_numbers():
    """Функция для генерации и вывода списка чисел"""
    global stop_flag
    print("---" * 18)
    print("Для остановки генерации, введите 0 и нажмите Enter")
    print("---" * 18)
    
    numbers = []
    
    # отслеживаниe ввода
    thread = threading.Thread(target=input_thread, daemon=True)
    thread.start()
    
    while not stop_flag:
        num = random.randint(0, 1000)
        numbers.append(num)
        print(num)
        time.sleep(2)
    
    # вывод списка 
    if len(numbers) > 1:
        print("\nСписок чисел:")
        #for n in numbers[:-1]:
        for n in numbers:
            print(n)
    #else:
        #print("\nНет чисел для отображения.")

if __name__ == "__main__":
    generate_numbers()