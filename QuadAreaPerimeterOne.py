if __name__ == '__main__':

    print("Calculating Area and Perimeter")

    length = float(input('Enter Length: '))
    width = float(input('Enter Width: '))

    area = length * width

    perimeter = 2 * (length + width)

    print(f'Length: {length}\nWidth: {width}')
    print(f'Area: {area}\nPerimeter: {perimeter}')