import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from keras.preprocessing import image

from keras.models import Sequential
from keras.layers import Dense, Activation


train_datagen = image.ImageDataGenerator(
        rescale=1./255)

test_datagen = image.ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        '../data/split/train',
        target_size=(150, 150),
        batch_size=32,
        class_mode='categorical',
)

validation_generator = test_datagen.flow_from_directory(
        '../data/split/val',
        target_size=(150, 150),
        batch_size=32,
        class_mode='categorical')


model = Sequential()
model.add(Dense(32, input_shape(150,150)))
model.add(Activation('softmax'))

model.fit_generator(
        train_generator,
        steps_per_epoch=2000,
        epochs=2,
        validation_data=validation_generator,
        validation_steps=800)

