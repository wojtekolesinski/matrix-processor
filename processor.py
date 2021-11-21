from matrix import Matrix

def choices():
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('0. Exit')

    try:
        choice = int(input('Your choice: '))
    except ValueError:
        print('Choice must be a single digit')
        return choices()

    if choice not in [1, 2, 3, 4, 5, 6, 0]:
        print('Not a viable choice')
        return choices()

    return choice


def trans_choices():
    print('1. Main diagonal')
    print('2. Side diagonal')
    print('3. Vertical line')
    print('4. Horizontal line')

    try:
        axis = int(input('Your choice: '))
    except ValueError:
        print('Choice must be a single digit')
        return trans_choices()

    if axis not in (1, 2, 3, 4):
        print('Not a viable choice')
        return trans_choices()

    if axis == 1:
        return 'main'
    if axis == 2:
        return 'side'
    if axis == 3:
        return 'vertical'
    if axis == 4:
        return 'horizontal'


def main():
    while True:
        choice = choices()

        if choice == 0:
            break

        if choice == 1:
            rows1, cols1 = [int(i) for i in input('Enter size of first matrix: ').split()]
            m1 = Matrix(rows1, cols1)
            print('Enter first matrix: ')
            m1.grab_elements()

            rows2, cols2 = [int(i) for i in input('Enter size of second matrix: ').split()]
            m2 = Matrix(rows2, cols2)
            print('Enter second matrix: ')
            m2.grab_elements()

            print('The result is: ')
            print(m1 + m2)

        elif choice == 2:
            rows1, cols1 = [int(i) for i in input('Enter matrix size: ').split()]
            m1 = Matrix(rows1, cols1)
            print('Enter matrix: ')
            m1.grab_elements()

            x = input('Enter constant:')
            x = int(x) if '.' not in x else float(x)

            print('The result is: ')
            print(m1 * x)

        elif choice == 3:
            rows1, cols1 = [int(i) for i in input('Enter size of first matrix: ').split()]
            m1 = Matrix(rows1, cols1)
            print('Enter first matrix: ')
            m1.grab_elements()

            rows2, cols2 = [int(i) for i in input('Enter size of second matrix: ').split()]
            m2 = Matrix(rows2, cols2)
            print('Enter second matrix: ')
            m2.grab_elements()

            print('The result is: ')
            print(m1 * m2)

        elif choice == 4:
            axis = trans_choices()
            rows1, cols1 = [int(i) for i in input('Enter matrix size: ').split()]
            m1 = Matrix(rows1, cols1)
            print('Enter matrix: ')
            m1.grab_elements()

            print('The result is: ')
            print(m1.transpose(axis))

        elif choice == 5:
            rows1, cols1 = [int(i) for i in input('Enter matrix size: ').split()]
            m1 = Matrix(rows1, cols1)
            print('Enter matrix: ')
            m1.grab_elements()

            print('The result is: ')
            print(m1.determinant())

        elif choice == 6:
            rows1, cols1 = [int(i) for i in input('Enter matrix size: ').split()]
            m1 = Matrix(rows1, cols1)
            print('Enter matrix: ')
            m1.grab_elements()

            print('The result is: ')
            print(m1.inverse())


if __name__ == '__main__':
    main()
