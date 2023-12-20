import sys


def circular_array_path(n, m):
    circular_array = list(range(1, n + 1))
    path = ''
    current_index = 0
    while True:
        path += str(circular_array[current_index])
        current_index = (current_index + m -1) % n
        if current_index == 0:
            break

    return path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Для запуска: python task1\\task1.py <n> <m>")
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        result_path = circular_array_path(n, m)
        print(result_path)