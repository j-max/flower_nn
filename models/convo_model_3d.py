import pandas as pd
import numpy as np
import os
import sys

import matplotlib.pyplot as plt
from keras.preprocessing import image


from keras.models import Sequential
from keras.layers import Dense, Activation, Conv3D, MaxPooling2D,MaxPool3D, Flatten


train_datagen = image.ImageDataGenerator(
        rescale=1./255)

test_datagen = image.ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'data/split/train/',
        target_size=(150, 150),
        batch_size=30,
        class_mode='categorical',
        color_mode='rgb'
)
 
validation_generator = test_datagen.flow_from_directory(

    'data/split/val',
        target_size=(150, 150),
        batch_size=30,
        color_mode='rgb',
        class_mode='categorical')


model = Sequential()

model.add(Conv3D(32, (3, 3), activation='relu',
                        input_shape=(150, 150, 3)))
model.add(MaxPooling3D((2, 2)))
model.add(Flatten())
model.add(Dense(5, activation='softmax'))

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit_generator(
        train_generator,
        steps_per_epoch=50,
        epochs=10,
        validation_data=validation_generator,
        validation_steps=50)

