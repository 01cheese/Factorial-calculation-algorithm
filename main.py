import concurrent.futures
import sys
import gmpy2
import os
import time
import subprocess

# Limit numerals for convert int to string
# Увеличиваем предел числа цифр для строкового представления целых чисел
sys.set_int_max_str_digits(10 ** 6)


# Function for starts process
# Функция для запуска процессов
def run_process(file_name, start, end, output_file):
    subprocess.run([sys.executable, file_name, str(start), str(end), output_file])


def multiply_final_results(result_files):
    final_result = gmpy2.mpz(1)
    for result_file in result_files:
        with open(result_file, 'r') as f:
            part_result = gmpy2.mpz(f.read())
            final_result *= part_result
    return final_result


if __name__ == '__main__':
    s = time.time()

    n = 5_000_000  # base factorial num

    ################

    num_files = 15
    # Quantity files worker_i.py, who work together
    # Количество файлов, которые будут запускаться параллельно


    # Create blocks for anyone files
    # Создаем блоки для каждого файла
    chunk_size = n // num_files
    result_files = []
    processes = []

    # Starts process
    # Запуск процессов
    for i in range(num_files):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i < num_files - 1 else n
        output_file = f"result_part_{i}.txt"
        result_files.append(output_file)

        process = subprocess.Popen([sys.executable, f"worker_{i}.py", str(start), str(end), output_file])
        processes.append(process)

    # Wait finish all process
    # Ожидаем завершения всех процессов
    for process in processes:
        process.wait()

    # Collect results and multiply their
    # Собираем результаты и перемножаем их
    final_result = multiply_final_results(result_files)

    f = time.time()

    print(f"Факториал числа {n} вычислен!")  # num
    print(f"Время выполнения: {f - s} секунд")  # time for calculus

    # After there: delete intermediate files
    # Опционально: удалить промежуточные файлы
    for result_file in result_files:
        os.remove(result_file)
