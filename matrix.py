import copy

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[] for i in range(self.rows)]

    def grab_elements(self):
        for i in range(self.rows):
            self.matrix[i] = [eval(el) for el in input().split()]

    def __add__(self, other):
        # checking, if other is also a matrix
        if isinstance(other, Matrix):
            #  checking, if matrices can be added
            if self.rows == other.rows and self.cols == other.cols:
                new_matrix = Matrix(self.rows, self.cols)
                for i in range(self.rows):
                    for j in range(self.cols):
                        new_matrix.matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
                return new_matrix
            else:
                print('ERROR')
        else:
            print('Object is not a matrix')

    def __mul__(self, other):
        """Multiplication function. Can handle matrix by matrix
        and matrix and matrix by constant multiplication"""
        # checking, if other is a number
        if isinstance(other, (int, float)):
            new_matrix = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.matrix[i].append(self.matrix[i][j] * other)
            return new_matrix
        # checking, if other is a matrix
        elif isinstance(other, Matrix):
            if self.cols == other.rows:
                new_matrix = Matrix(self.rows, other.cols)
                for i in range(new_matrix.rows):
                    for j in range(new_matrix.cols):
                        x = 0
                        for k in range(self.cols):
                            x += self.matrix[i][k] * other.matrix[k][j]
                        new_matrix.matrix[i].append(x)

                return new_matrix
            else:
                print('The operation cannot be performed.')

    def __repr__(self):
        """printable representation of a matrix"""
        representation = ''''''
        for i in range(self.rows):
            for j in range(self.cols):
                # representation += str(round(self.matrix[i][j], 2)) + ' '
                representation += str(self.matrix[i][j]) + ' '
            representation += '\n'
        return representation

    def transpose(self, axis):
        """Matrix transposition function, taking the axis as an argument.
        It can do transpose a matrix along main and side diagonals, and horizontal and vertical axes"""
        new_matrix = Matrix(self.cols, self.rows)
        new_matrix.matrix = [[None for i in range(new_matrix.cols)] for j in range(new_matrix.rows)]

        if axis == 'main':
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.matrix[j][i] = self.matrix[i][j]
            return new_matrix

        if axis == 'side':
            return self.transpose('vertical').transpose('main').transpose('vertical')

        if axis == 'vertical':
            for i in range(self.rows):
                counter = -1
                for j in range(self.rows):
                    new_matrix.matrix[i][j] = self.matrix[i][counter]
                    counter -= 1
            return new_matrix

        if axis == 'horizontal':
            counter = -1
            for i in range(self.rows):
                new_matrix.matrix[i] = self.matrix[counter]
                counter -= 1
            return new_matrix

    def determinant(self):
        """Function computing a determinant of the matrix. It has three base cases,
        and a recursive case, when the matrix is bigger, than 2 by 2"""
        if self.rows != self.cols:
            print('Cannot calculate a determinant')
            return

        if self.rows == 1:
            return self.matrix[0][0]

        if self.rows == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

        result = 0
        for k in range(self.cols):
            new_matrix = Matrix(self.rows - 1, self.cols - 1)
            temp_array = [[] for i in range(self.rows)]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    temp_array[i].append(self.matrix[i][j])
            for row in temp_array:
                row.pop(k)

            new_matrix.matrix = [el for el in temp_array[1:]]
            result += self.matrix[0][k] * new_matrix.determinant() * (-1)**(0+k)

        return result

    def inverse(self):
        det = self.determinant()

        if det in (0, None):
            print('Cannot invert matrix')
            return

        adjoint = Matrix(self.rows, self.cols)
        adjoint.matrix = [[None for i in range(self.cols)] for j in range(self.rows)]


        for i in range(self.rows):
            for j in range(self.cols):
                temp_array = copy.deepcopy(self.matrix)

                for row in temp_array:
                    row.pop(j)
                temp_array.pop(i)
                new_mx = Matrix(self.rows - 1, self.cols - 1)
                new_mx.matrix = temp_array
                adjoint.matrix[i][j] = new_mx.determinant() * (-1) ** (j + i)

        adjoint = adjoint.transpose('main')

        return adjoint * (1 / det)
