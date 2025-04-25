from random import random

class Matrix:
    def __init__(self, array):
        """
        Initialize the matrix with a given array.
        """
        self._data = [row for row in array]
        self.shape = [len(array), len(array[0])]

    @staticmethod
    def zeroes(shape):
        """
        Return a matrix of zeroes with the given shape.
        """
        return Matrix([[0 for _ in range(shape[1])] for _ in range(shape[0])])

    def ones(shape):
        """
        Return a matrix of ones with the given shape.
        """
        return Matrix([[1 for _ in range(shape[1])] for _ in range(shape[0])])

    def random(shape):
        """
        Return a matrix with random values in the given shape.
        """
        return Matrix([[random() for _ in range(shape[1])] for _ in range(shape[0])])

    def getitem(self, row, col):
        """
        Get the value at the specified row and column.
        """
        return self._data[row][col]

    def setitem(self, row, col, value):
        """
        Set the value at the specified row and column.
        """
        self._data[row][col] = value

    def transpose(self):
        """
        Transpose the matrix.
        """
        tData = Matrix.zeroes(self.shape[1],self.shape[0])
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                tData.setitem(j,i,self.getitem(i,j))
        return tData


    def scaler_multiply(self, value):
        """
        Multiply the matrix by a scalar value.
        """
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self.setitem(i,j,self.getitem(i,j)*value)

    def multiply(self, mat):
        """
        Multiply elementwise the matrix by another matrix.
        """
        if self.shape != mat.shape:
            return "Incompatible shapes"
        out = Matrix.zeros(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                out.setitem(i,j,self.getitem(i,j)*mat.getitem(i,j))
        


    def divide(self, mat):
        """
        Divide the matrix by another matrix.
        """
        if self.shape != mat.shape:
            return "Incompatible shapes"
        out = Matrix.zeros(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                out.setitem(i,j,self.getitem(i,j) / mat.getitem(i,j))

    def sum(self):
        """
        Return the sum of all elements in the matrix.
        """
        total = 0
        for row in self._data:
            for item in row:
                total += item
        return total

    def __add__(self, mat):
        """
        Add another matrix to this matrix.
        """
        if self.shape != mat.shape:
            return "Incompatible shapes"
        out = Matrix.zeros(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                out.setitem(i,j,self.getitem(i,j) + mat.getitem(i,j))
        return out


    def __sub__(self, mat):
        """
        Subtract another matrix from this matrix.
        """
        return self.__add__(mat.scalar_multiply(-1))

    def __matmul__(self, mat):
        """
        Matrix multiplication with another matrix.
        """
        out = [[0 for _ in range(mat.shape[1])] for _ in range(len(self._data))]
        for j in range(mat.shape[1]):
            for i in range(len(self._data)):
                for k in range(mat.shape[0]):
                    out[i][j] += self.getitem(i,k) * mat.getitem(k,j)
        return Matrix(out)

    def __mul__(self, other):
        """
        Multiply the matrix element-wise by another matrix or a scalar.
        """
        return self.multiply(other)

    def truediv(self, other):
        """
        Divide the matrix element-wise by another matrix or a scalar.
        """
        return self.divide(other)

    def __str__(self):
        """
        Return a string representation of the matrix.
        """
        return '\n'.join([str(row) for row in self._data])