import concurrent.futures
import sys
import time
import gmpy2
import os

# Увеличиваем предел числа цифр для строкового представления целых чисел
sys.set_int_max_str_digits(10 ** 6)

# Функция для перемножения элементов внутри блока с использованием gmpy2
def multiply_chunk(chunk):
    result = gmpy2.mpz(1)
    for number in chunk:
        result *= number
    return result

def generate_initial_list(n):
    return list(range(1, n + 1))

def chunked_multiply(lst, chunk_size):
    # Разбиваем список на блоки и параллельно обрабатываем их
    chunks = (lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size))

    # Используем многопроцессорный пул для параллельного умножения блоков
    with concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        results = list(executor.map(multiply_chunk, chunks))

    return results

def process_list(lst):
    chunk_size = max(100000, len(lst) // os.cpu_count())  # Оптимизируем размер блока
    while len(lst) > 1:
        lst = chunked_multiply(lst, chunk_size)
    return lst[0]

if __name__ == '__main__':
    # Основная часть программы
    s = time.time()

    # Генерация списка чисел
    n = 1_000_000
    initial_list = generate_initial_list(n)

    # Обработка списка (вычисление факториала через блочное перемножение)
    final_result = process_list(initial_list)

    f = time.time()

    print(f"Факториал числа {n} вычислен!")
    print(f"Время выполнения: {f - s} секунд")
