from abc import ABC, abstractmethod


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
