from tensorflow.keras.preprocessing import image_dataset_from_directory
import numpy as np
from tensorflow import keras as tf
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn import metrics as m
from keras.models import Sequential
import keras

train_ds = image_dataset_from_directory(
    directory='gtsrb_dataset/Train/',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48))


test_ds = image_dataset_from_directory(
    directory='gtsrb_dataset/Test_dir/',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48))


#Zad3
model = Sequential()

model.add(keras.Input(shape = (48, 48, 3)))
model.add(layers.Conv2D(32, 3, activation = 'relu'))
model.add(layers.Conv2D(32, 3, activation = 'relu'))
model.add(layers.MaxPooling2D(2))
tf.keras.layers.Dropout(.2)

model.add(layers.Conv2D(64, 3, activation = 'relu'))
model.add(layers.Conv2D(64, 3, activation = 'relu'))
model.add(layers.MaxPooling2D(2))
tf.keras.layers.Dropout(.2)

model.add(layers.Conv2D(128, 3, activation = 'relu'))
model.add(layers.Conv2D(128, 3, activation = 'relu'))
model.add(layers.MaxPooling2D(2))
tf.keras.layers.Dropout(.2)

model.compile(loss='categorical_crossentropy',optimizer='sgd', metrics=['accuracy'])
model.summary()

#učenje mreže
model.fit(train_ds, test_ds, epochs = 5, batch_size = 32)

predict = model.predict(test_ds, batch_size = 128)

print(m.confusion_matrix(test_ds, predict))



