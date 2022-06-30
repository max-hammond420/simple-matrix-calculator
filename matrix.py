import os

class Matrix:

    def __init__(self, filename=''):

        if os.path.exists(filename):
            self.matrix = []
            with open(filename) as f:
                for x in f:
                    if x != '\n':
                        self.matrix.append(list(map(int, x.split())))

        else:
            self.matrix = [[0, 0, 0],
            [1, 1, 1],
            [2, 2, 2]]

        self.rows = len(self.matrix[0])
        self.columns = len(self.matrix)


    def add(self, other):
        m = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            m.append(row)
        return class_instance(m)


    def scale(self, c):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] *= c
        return class_instance(self.matrix)


    def transpose(self):
        m = []
        for i in range(len(self.matrix[0])):
            rows = []
            for j in range(len(self.matrix)):
                rows.append(self.matrix[j][i])
            m.append(rows)
        return class_instance(m)


    def make_2d(self):
        return self.matrix


    def multiply(self, other):
        m = []
        if self.columns != other.rows:
            print("Can't multiply matrices")
            return None
        new_m = other.transpose().make_2d()
        for i in range(self.rows):
            rows = []
            for j in range(other.columns):
                rows.append(dot_product(self.matrix[i], new_m[j]))
            m.append(rows)
        return class_instance(m)


    def __repr__(self):
        s = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                s += str(self.matrix[i][j]) + ' '
            s += '\n'
        return s


def dot_product(a, b):
    # a and b are both 1 dimensional matrices with same length
    total = 0
    for i in range(len(a)):
        total += (a[i] * b[i])
    return total

def class_instance(m):
    # takes in a matrix, m, as a 2d array and returns a Matrix class
    with open('output.txt', 'w') as f:
        for i in range(len(m)):
            for j in range(len(m[i])):
                f.write(str(m[i][j]) + ' ')
            f.write('\n')
    return Matrix('output.txt')
