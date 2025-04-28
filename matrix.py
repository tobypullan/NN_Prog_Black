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

    @staticmethod
    def ones(shape):
        """
        Return a matrix of ones with the given shape.
        """
        return Matrix([[1 for _ in range(shape[1])] for _ in range(shape[0])])

    @staticmethod
    def random(shape):
        """
        Return a matrix with random values in the given shape.
        """
        return Matrix([[random() - 0.5 for _ in range(shape[1])] for _ in range(shape[0])])

    def __getitem__(self, idx):
        """
        Get the value at the specified row and column.
        """
        
        row, col = idx
        return self._data[row][col]

    def __setitem__(self, idx, value):
        """
        Set the value at the specified row and column.
        """
        
        row, col = idx
        self._data[row][col] = value

    def transpose(self):
        """
        Transpose the matrix.
        """
        
        tData = Matrix.zeroes(self.shape[1],self.shape[0])
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                tData[j, i] = self[i, j]
                
        return tData

    def scaler_multiply(self, value):
        """
        Multiply the matrix by a scalar value.
        """
        
        out = Matrix.zeroes(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                out[i, j] = self[i, j] * value
                
        return out

    def multiply(self, mat):
        """
        Multiply elementwise the matrix by another matrix.
        """
        if self.shape != mat.shape:
            return "Incompatible shapes"
        
        out = Matrix.zeros(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                out[i, j] = self[i, j] * mat[i, j]
                
        return out

    def divide(self, mat):
        """
        Divide the matrix by another matrix.
        """
        if self.shape != mat.shape:
            return "Incompatible shapes"
        
        out = Matrix.zeros(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                out[i, j] = self[i, j] / mat[i, j]
                
        return out

    def sum(self,axis=None):
        """
        Return the sum of all elements in the matrix.

        axis = 0 sum across cols
        axis = 1 sum across rows
        """
        if axis == None:
            total = 0
            
            for row in self._data:
                total += sum(row)
                
            return total
        
        elif axis == 0:
            out = Matrix.zeroes(self.shape[0], 1)
            
            for idx, row in enumerate(self._data):
                out[idx, 0] = sum(row)
                
            return out
        
        elif axis == 1:
            out = Matrix.zeroes(1, self.shape[1])
            
            for idx, row in enumerate(self._data):
                for jdx, val in enumerate(row):
                    out[0, jdx] += val
                    
            return out
        else:
            return "invalid axis"
    
    def vec_add(self, vec):
        """
        broadcasts vec to number of cols of mat then adds together
        """
        out = Matrix.zeroes(self.shape)
        
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                out[i, j] = self[i, j] + vec[i, 0]
                
        return out

    def vec_sub(self, vec):
        self.vec_add(vec.scalar_multiply(-1))

    def __add__(self, mat):
        """
        Add another matrix to this matrix.
        """
        if self.shape != mat.shape:
            return "Incompatible shapes"
        
        out = Matrix.zeros(self.shape)
        
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                out[i, j] = self[i, j] + mat[i, j]
                
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
            for k in range(mat.shape[0]):
                for i in range(len(self._data)):
                    out[i][j] += self[i, k] * mat[k, j]
                    
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
    
    def concat(self, mat, axis):
        """
        Concatenate this matrix with another matrix along the specified axis.
        axis=0: concatenate vertically (combine rows)
        axis=1: concatenate horizontally (combine columns)
        """
        if axis == 1:
            # Check if columns match
            if self.shape[1] != mat.shape[1]:
                return "Incompatible shapes for vertical concatenation"
            
            # Create new data by combining rows
            new_data = self._data + mat._data
            return Matrix(new_data)
        
        elif axis == 0:
            # Check if rows match
            if self.shape[0] != mat.shape[0]:
                return "Incompatible shapes for horizontal concatenation"
            
            # Create new data by combining columns
            new_data = []
            for i in range(self.shape[0]):
                row = self._data[i] + mat._data[i]
                new_data.append(row)
            
            return Matrix(new_data)
        
        else:
            return "Invalid axis. Use 0 for vertical or 1 for horizontal concatenation."

    def map(self, func):
        """
        Apply a function to all elements of the matrix and return a new matrix.
        """
        result = Matrix.zeroes(self.shape)
        
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                result[i, j] = func(self[i, j])
                
        return result