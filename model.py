class Model:
    def __init__(self, layers):
      pass
  
    def connect(self, layer):
        pass
    
    def predict(self, x):
      pass
  
    def backpropagate(self, prediction, y, loss_function):
        pass
    
    def train(
        self, 
        x, 
        y, 
        loss_function, 
        epochs, 
        batch_size, 
        learning_rate=0.001, 
        log_interval=1
        ):
        pass