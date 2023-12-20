import sys


def read_input(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]


def min_moves_to_equal(nums):
    total_moves = 0
    target = sum(nums) // len(nums)

    for num in nums:
        total_moves += abs(num - target)

    return total_moves


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Для запуска: python task4\\task4.py task4\\data.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    nums = read_input(input_file)
    result = min_moves_to_equal(nums)

    print(result)
