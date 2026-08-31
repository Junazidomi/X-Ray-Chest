from tensorflow.keras import Model, layers
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout, BatchNormalization

def modeling():
    model=Sequential()
    
    model.add(Conv2D(32,(3,3), padding='same', activation='relu', input_shape=(150, 150,3)))
    model.add(Conv2D(32, (3,3), activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(2,2))
    model.add(Dropout(0.3))

    model.add(Conv2D(64,(5,5), padding='same',activation='relu'))
    model.add(Conv2D(64, (5,5), activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(2,2))
    model.add(Dropout(0.3))

    model.add(Conv2D(128, (7,7), padding='same', activation='relu'))
    model.add(Conv2D(128, (7,7), activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(2,2))
    model.add(Dropout(0.3))

    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.3))

    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))

    model.add(Dense(1, activation='sigmoid'))

    model.compile(
        optimizer=RMSprop(),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model
