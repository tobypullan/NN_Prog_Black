from layers import DenseLayer, Tanh
import matplotlib.pyplot as plt
from matrix import Matrix
from math import pi, sin
from model import Model
from loss import MSE

X = []
i = 0
while i < 2 * pi:
    X.append(i)
    i += 0.01

Y = [sin(i) for i in X]

X_train = list(map(lambda x: Matrix([[x]]), X))
Y_train = list(map(lambda y: Matrix([[y]]), Y))

model = Model(1)
model.connect(DenseLayer(32))
model.connect(Tanh())
model.connect(DenseLayer(32))
model.connect(Tanh())
model.connect(DenseLayer(1))

model.train(
  X_train,
  Y_train,
  loss_function=MSE(),
  epochs=50,
  batch_size=1,
  learning_rate=0.01,
  log_interval=1
)

predictions = [model.predict(x).sum() for x in X_train]

plt.plot(X, Y, label="True Function")
plt.plot(X, predictions, label="Predictions")
plt.legend()

plt.show()