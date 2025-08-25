from math import pi


def calculate_radius(r: float) -> float:
    return pi * r ** 2


if __name__ == '__main__':
    radius: float = float(input('Enter Circle Radius: '))
    circle_area: float = calculate_radius(3)
    print(f'{circle_area}')
