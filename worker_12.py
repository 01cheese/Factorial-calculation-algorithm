import sys
import gmpy2

def multiply_range(start, end):
    result = gmpy2.mpz(1)
    for number in range(start, end + 1):
        result *= number
    return result

if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    output_file = sys.argv[3]

    # Выполняем умножение чисел в указанном диапазоне
    result = multiply_range(start, end)

    # Записываем результат в файл
    with open(output_file, 'w') as f:
        f.write(str(result))
