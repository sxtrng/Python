"""
        Counting Evens and Odds
"""


if __name__ == '__main__':
    numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    length = len(numbers)
    evens = 0
    odds = 0

    for number in numbers:
        if number % 2 == 0:
            evens += 1
        elif number % 2 == 1:
            odds += 1

    print(f'Length of List: {length}')
    print(f'Number of occurrences of an even number: {evens}')
    print(f'Number of occurrences of an odd number: {odds}')