from matrix import Matrix
class MSE: # mean square error loss function
    def __call__(self, prediction, y):
        """
        perform MSE calculation on prediction and y (both matrix objects)
        """
        return (prediction - y).map(lambda x: x**2)
    def derivative(self, prediction, y):
        """
        used in backpropagation, derivative of loss
        """
        return (prediction - y).scalar_multiply(2)