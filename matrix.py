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
        for i in range(len(self._data)):
            for j in range(len(self._data[0])):
                self.setitem(i,j,self.getitem(i,j)*value)

    def multiply(self, mat):
        """
        Multiply the matrix by another matrix.
        """
        out = [[0 for _ in range(mat.shape[1])] for _ in range(len(self._data))]
        for j in range(mat.shape[1]):
            for i in range(len(self._data)):
                for k in range(mat.shape[0]):
                    out[i][j] += self.getitem(i,k) * mat.getitem(k,j)
        return Matrix(out)


    def divide(self, mat):
        """
        Divide the matrix by another matrix.
        """
        pass

    def sum(self):
        """
        Return the sum of all elements in the matrix.
        """
        total = 0
        for row in self._data:
            for item in row:
                total += item
        return total

    def add(self, mat):
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


    def sub(self, mat):
        """
        Subtract another matrix from this matrix.
        """
        return self.add(mat.scalar_multiply(-1))

    def matmul(self, mat):
        """
        Matrix multiplication with another matrix.
        """
        pass

    def mul(self, other):
        """
        Multiply the matrix element-wise by another matrix or a scalar.
        """
        pass

    def truediv(self, other):
        """
        Divide the matrix element-wise by another matrix or a scalar.
        """
        pass

    def str(self):
        """
        Return a string representation of the matrix.
        """
        pass