import pandas as pd
import numpy as np
import os
import sys
sys.path.insert(0,'.')
import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Flatten
from sklearn.metrics import classification_report, recall_score
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import seaborn as sns

train_datagen = image.ImageDataGenerator(
        rescale=1./255)

test_datagen = image.ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'data/split/train',
        target_size=(150, 150),
        batch_size=100,
        class_mode='categorical',
        color_mode='grayscale'
)

validation_generator = test_datagen.flow_from_directory(
    'data/split/val',
        target_size=(150, 150),
        batch_size=30,
        color_mode='grayscale',
        class_mode='categorical')

train_images, train_labels = next(train_generator)
val_images, val_labels = next(validation_generator)
train_img = train_images.reshape(train_images.shape[0], -1)
val_img = val_images.reshape(val_images.shape[0], -1)

model = Sequential()

model.add(Dense(32, activation='relu', input_shape=(22500,)))
model.add(Dense(16, activation='relu', ))
model.add(Dense(8, activation='relu', ))
model.add(Dense(5, activation='softmax'))

model.compile(optimizer='Adam', loss='categorical_crossentropy',   metrics=['acc'])

model.fit(
        train_img, train_labels,
        epochs=10,
        validation_data=(val_img, val_labels),
        )

y_hat_train = model.predict_classes(train_img)

# generator creates labels in one-hot array, so we have to convert predictions as well

ohe=OneHotEncoder(sparse=False)
# Can't fit on the predictions, because too often predictions don't predict categories
ohe.fit(np.array([0,1,2,3,4]).reshape(-1,1))
y_hat_train_enc=ohe.transform(y_hat_train.reshape(-1,1))

# Have to make recall score micro for 5 class labels
print(recall_score(train_labels, y_hat_train_enc, average='micro'))

train_accuracy = model.history.history['acc']
train_loss= model.history.history['loss']
val_accuracy = model.history.history['val_acc']
val_loss= model.history.history['val_loss']
epochs   = model.history.epoch

# Right now, for our FSM, the accuracy is still very low, at about .3
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5))
ax1.plot(epochs, train_accuracy, label='train_acc')
ax1.plot(epochs, val_accuracy,  label='val_acc')
ax2.plot(epochs, train_loss,  label='train_loss')
ax2.plot(epochs, val_loss,  label='val_loss')
ax1.legend()
ax2.legend()
plt.show()
