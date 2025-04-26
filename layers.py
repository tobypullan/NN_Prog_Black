from abc import ABC, abstractmethod
from matrix import Matrix


class Layer(ABC):
    @abstractmethod
    def setup(self, input_neurons, batch_size):
        """
        Initialize the weights and biases for the layer
        """
        pass
    
    @abstractmethod
    def forward(self, in_matrix):
        """
        Perform the forward pass for the layer
        """
        pass
    
    @abstractmethod
    def backward(self, gradients):
        """
        Perform the backward pass for the layer
        """
        pass
    
    @property
    @abstractmethod
    def neurons(self):
        """
        Return the number of neurons in the layer
        """
        pass
    
    
class DenseLayer(Layer):
    def __init__(self, neurons):
        self._neurons = neurons
        self.batch_size = None
        self.weights = None
        self.biases = None
        self.in_matrix = None
        self.dw = None
        self.db = None
        
    def setup(self, input_neurons, batch_size):
        self.weights = Matrix.random((self._neurons, input_neurons))
        self.biases = Matrix.random((self._neurons, 1))
        self.batch_size = batch_size
        
    def forward(self, in_matrix):
        self.in_matrix = in_matrix
        return self.weights @ in_matrix + self.biases
    
    def backward(self, gradients, learning_rate):
        self.dw = gradients @ self.in_matrix.transpose() * 1 / self.batch_size
        self.db = gradients.sum(axis=0) * 1 / self.batch_size
        
        self.weights = self.weights - self.dw * learning_rate
        self.biases = self.biases - self.db * learning_rate
        
        return self.weights.transpose() @ gradients
    
    @property
    def neurons(self):
        return self._neurons
