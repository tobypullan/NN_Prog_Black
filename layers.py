from abc import ABC, abstractmethod
from matrix import Matrix
from math import exp


class Layer(ABC):
    @abstractmethod
    def setup(self, input_neurons):
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
        
    def setup(self, input_neurons):
        self.weights = Matrix.random((self._neurons, input_neurons))
        self.biases = Matrix.random((self._neurons, 1))
        
    def forward(self, in_matrix):
        self.in_matrix = in_matrix
        return self.weights @ in_matrix + self.biases
    
    def backward(self, gradients, learning_rate):
        self.dw = gradients @ self.in_matrix.transpose() * 1 / self.in_matrix.shape[1]
        self.db = gradients.sum(axis=0) * 1 / self.in_matrix.shape[1]
        
        self.weights = self.weights - self.dw * learning_rate
        self.biases = self.biases - self.db * learning_rate
        
        return self.weights.transpose() @ gradients
    
    @property
    def neurons(self):
        return self._neurons
    

class ActivationLayer(Layer):
    def setup(self, input_neurons):
        self._neurons = input_neurons
        
    def forward(self, in_matrix):
        self.in_matrix = in_matrix
        return self(in_matrix)
    
    def backward(self, gradients):
        return gradients * self.derivative(self.in_matrix)
    
    @property
    def neurons(self):
        return self._neurons
    
    @abstractmethod
    def __call__(self, in_matrix):
        """
        Apply the activation function to the input matrix
        """
        pass
    
    @abstractmethod
    def derivative(self, in_matrix):
        """
        Compute the derivative of the activation function
        """
        pass
    
    
class ReLU(ActivationLayer):
    def __call__(self, in_matrix):
        return in_matrix.map(lambda x: max(0, x))
    
    def derivative(self, in_matrix):
        return in_matrix.map(lambda x: 1 if x > 0 else 0)
    
    
class Sigmoid(ActivationLayer):
    def __call__(self, in_matrix):
        return in_matrix.map(self.sigmoid)
    
    def derivative(self, in_matrix):
        return in_matrix.map(lambda x: self.sigmoid(x) * (1 - self.sigmoid(x)))
    
    def sigmoid(self, x):
        return 1 / (1 + exp(-x))
