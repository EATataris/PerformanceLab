import sys
import math


def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        x, y = map(float, lines[0].split())
        radius = float(lines[1])
        return (x, y), radius


def read_points(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [tuple(map(float, line.split())) for line in lines]


def point_position(center, radius, point):
    distance_squared = (point[0] - center[0])**2 + (point[1] - center[1])**2

    if math.isclose(distance_squared, radius**2):
        return 0
    elif distance_squared < radius**2:
        return 1
    else:
        return 2


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Для запуска: python task2\\task2.py task2\\файл1.txt task2\\файл2.txt")
        sys.exit(1)

    circle_data = read_circle_data(sys.argv[1])
    points = read_points(sys.argv[2])

    for point in points:
        position = point_position(circle_data[0], circle_data[1], point)
        print(position)
