class Matrix:
    def init(array):
        """
        Initialize the matrix with a given array.
        """
        pass

    @staticmethod
    def zeroes(shape):
        """
        Return a matrix of zeroes with the given shape.
        """
        pass

    def ones(shape):
        """
        Return a matrix of ones with the given shape.
        """
        pass

    def random(shape):
        """
        Return a matrix with random values in the given shape.
        """
        pass

    def getitem(self, row, col):
        """
        Get the value at the specified row and column.
        """
        pass

    def setitem(self, row, col, value):
        """
        Set the value at the specified row and column.
        """
        pass

    def transpose(self):
        """
        Transpose the matrix.
        """
        pass

    def scaler_multiply(self, value):
        """
        Multiply the matrix by a scalar value.
        """
        pass

    def multiply(self, mat):
        """
        Multiply the matrix by another matrix.
        """
        pass

    def divide(self, mat):
        """
        Divide the matrix by another matrix.
        """
        pass

    def sum(self, axis):
        """
        Return the sum of all elements in the matrix, possibilty along a certain axis.
        """
        pass

    def add(self, mat):
        """
        Add another matrix to this matrix.
        """
        pass

    def sub(self, mat):
        """
        Subtract another matrix from this matrix.
        """
        pass

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
    
    def concat(self, mat, axis):
        """
        Concatenate this matrix with another matrix along the specified axis.
        """
        pass
    
    def vec_add(self, vec):
        """
        Add a vector to the matrix.
        """
        pass
    
    def vec_sub(self, vec):
        """
        Subtract a vector from the matrix.
        """
        pass
    
    def map(self, func):
        """
        Apply a function to each element of the matrix.
        """
        pass