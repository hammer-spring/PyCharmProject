import pandas as pd
import numpy as np
import os

data = pd.read_csv(r'D:\PyCharm\PyCharmProject\从零开始学python网络爬虫\爬去大乐透号码并预测\data_recent.csv', sep=' ', header=None, error_bad_lines=False).values
data = data[:, 2:]
mean = data[:1500].mean(axis=0)
std = data[:1500].std(axis=0)
data1 = data.copy()
data1 -= mean
data1 /= std
train_data = data1[:1400]
train_data = np.expand_dims(train_data, axis=1)
val_data = data1[1400:1550]
val_data = np.expand_dims(val_data, axis=1)
test_data = data1[1550:len(data) - 1]
test_data = np.expand_dims(test_data, axis=1)
red1_labels = data[:, 0]
red2_labels = data[:, 1]
red3_labels = data[:, 2]
red4_labels = data[:, 3]
red5_labels = data[:, 4]
blue1_labels = data[:, 5]
blue2_labels = data[:, 6]
train_labels_1 = red1_labels[1:1401]
train_labels_2 = red2_labels[1:1401]
train_labels_3 = red3_labels[1:1401]
train_labels_4 = red4_labels[1:1401]
train_labels_5 = red5_labels[1:1401]
train_labels_6 = blue1_labels[1:1401]
train_labels_7 = blue2_labels[1:1401]
val_labels_1 = red1_labels[1401:1551]
val_labels_2 = red2_labels[1401:1551]
val_labels_3 = red3_labels[1401:1551]
val_labels_4 = red4_labels[1401:1551]
val_labels_5 = red5_labels[1401:1551]
val_labels_6 = blue1_labels[1401:1551]
val_labels_7 = blue2_labels[1401:1551]
test_labels_1 = red1_labels[1551:]
test_labels_2 = red2_labels[1551:]
test_labels_3 = red3_labels[1551:]
test_labels_4 = red4_labels[1551:]
test_labels_5 = red5_labels[1551:]
test_labels_6 = blue1_labels[1551:]
test_labels_7 = blue2_labels[1551:]
from keras import layers
from keras import Model
from keras import Input
from keras.optimizers import RMSprop

post_input = Input(shape=(None, 7), name='post_input')
lstm = layers.LSTM(150, dropout=0.2, recurrent_dropout=0.2, activation='relu', return_sequences=True)(post_input)
lstm1 = layers.LSTM(250, dropout=0.2, recurrent_dropout=0.2, activation='relu')(lstm)
x = layers.Dense(360, activation='relu')(lstm1)
x = layers.Dense(250, activation='relu')(x)
x = layers.Dense(250, activation='relu')(x)
x = layers.Dense(250, activation='relu')(x)
x = layers.Dense(250, activation='relu')(x)
x = layers.Dense(250, activation='relu')(x)
x = layers.Dense(140, activation='relu')(x)
x = layers.Dense(70, activation='relu')(x)
# x=layers.Dropout(0.3)(x)
red1_predict = layers.Dense(1, name='red1')(x)
red2_predict = layers.Dense(1, name='red2')(x)
red3_predict = layers.Dense(1, name='red3')(x)
red4_predict = layers.Dense(1, name='red4')(x)
red5_predict = layers.Dense(1, name='red5')(x)
blue1_predict = layers.Dense(1, name='blue1')(x)
blue2_predict = layers.Dense(1, name='blue2')(x)
model = Model(post_input,
              [red1_predict, red2_predict, red3_predict, red4_predict, red5_predict, blue1_predict, blue2_predict])
model.compile(optimizer=RMSprop(1e-4), loss=['mse', 'mse', 'mse', 'mse', 'mse', 'mse', 'mse'],
              metrics=['acc', 'acc', 'acc', 'acc', 'acc', 'acc', 'acc'])
history = model.fit(train_data,
                    [train_labels_1, train_labels_2, train_labels_3, train_labels_4, train_labels_5, train_labels_6,
                     train_labels_7],
                    batch_size=20, epochs=50,
                    validation_data=(val_data, [val_labels_1, val_labels_2, val_labels_3, val_labels_4, val_labels_5,
                                                val_labels_6, val_labels_7]))
import matplotlib.pyplot as plt

loss = history.history['loss']
loss = loss[3:]
val_loss = history.history['val_loss']
val_loss = val_loss[3:]
epochs = range(1, len(loss) + 1)
plt.figure()
plt.plot(epochs, loss, 'b', color='r', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()

