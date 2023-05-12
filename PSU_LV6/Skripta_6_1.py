import numpy as np
from sklearn.datasets import fetch_openml
import joblib
import pickle
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from sklearn import metrics as m

X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)


# TODO: prikazi nekoliko ulaznih slika
image = X[:1].reshape((28, 28))
plt.imshow(image, cmap='gray')
plt.show()

# skaliraj podatke, train/test split
X = X / 255.
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]


# TODO: izgradite vlastitu mrezu pomocu sckitlearn MPLClassifier 
mlp_mnist = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='adam', alpha=0.001, max_iter=50, learning_rate_init=0.01)
mlp_mnist.fit(X_train, y_train)

# TODO: evaluirajte izgradenu mrezu
y_predict = mlp_mnist.predict(X_test)
print(m.confusion_matrix(y_train[:10000], y_predict))
print(m.classification_report(y_test, y_predict))
print(m.confusion_matrix(y_test, y_predict))

#4) Na prvih 10000 train podataka, confusion_matrix ne raspoznaje brojeve
# Na test podacima raspoznaje uz malu pojavu zabuna

#spremi mrezu na disk
filename = "NN_model.sav"
joblib.dump(mlp_mnist, filename)
