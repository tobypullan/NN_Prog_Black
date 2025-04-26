class Model:
    def __init__(self, input_neurons):
        pass
        
    def connect(self, layer):
        pass
        
    def predict(self, in_matrix):
        pass
    
    def backpropagate(self, gradients, learning_rate):
        pass
    
    def train(
        self, 
        x_train, 
        y_train,
        loss_function,
        epochs,
        batch_size,
        learning_rate=0.01,
        log_interval=1,
        ):
        pass