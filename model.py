from random import shuffle

class Model:
    def __init__(self, input_units):
      self.input_units = input_units
      self.layers = []
  
    def connect(self, layer):
        layer.setup(self.input_units if not self.layers else self.layers[-1].neurons)
        self.layers.append(layer)
    
    def predict(self, x):
      result = x
      
      for layer in self.layers:
        result = layer.forward(result)
        
      return result
  
    def backpropagate(self, predictions, labels, loss_function, learning_rate):
        loss = loss_function(predictions, labels)
        gradients = loss_function.derivative(predictions, labels)
        
        for layer in self.layers[::-1]:
            gradients = layer.backward(gradients, learning_rate=learning_rate)
            
        return loss
    
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
        zipped = list(zip(x, y))
        shuffle(zipped)
        x, y = zip(*zipped)
        
        x_batches = []
        y_batches = []
        for start in range(0, len(x), batch_size):
            end = min(start + batch_size, len(x))
            
            x_samples = x[start:end]
            y_samples = y[start:end]
            
            x_batch = x_samples[0]
            y_batch = y_samples[0]
            for x_sample, y_sample in zip(x_samples[1:], y_samples[1:]):
                x_batch = x_batch.concat(x_sample)
                y_batch = y_batch.concat(y_sample)
                
            x_batches.append(x_batch)
            y_batches.append(y_batch)
        
        for epoch in range(epochs):
            epoch_loss = 0
            for x_batch, y_batch in zip(x_batches, y_batches):
                predictions = self.predict(x_batch)
                loss = self.backpropagate(predictions, y_batch, loss_function, learning_rate)
                average_loss = loss.sum(axis=1) / x_batch.shape[1]
                epoch_loss += average_loss.sum()
                
            if epoch % log_interval == 0:
                print(f"Epoch {epoch}, Loss: {loss}")