from keras.applications import VGG16
from keras.models import Sequential
from keras.layers import Conv2D, Flatten, Dense, MaxPooling2D, Dropout
from keras.regularizers import l2
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator

NUM_CLASSES = 10

def train_and_eval_CNN(X_train, y_train, X_val, y_val, X_test, y_test):
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(32,32,1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(NUM_CLASSES, activation='softmax'))

    # Compile the model
    model.compile(
        loss='categorical_crossentropy',
        optimizer=RMSprop(learning_rate=1e-4),
        metrics=['accuracy']
    )

    # Display the model structure
    model.summary()

    # Create a data generator for the data augmentation
    datagen = ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        brightness_range=[0.2, 1.0],
        horizontal_flip=True,
        vertical_flip=True,
        channel_shift_range=0.5,
    )

    # Adjust the generator to the training data
    datagen.fit(X_train)

    # Train the model with data augmentation
    model.fit(datagen.flow(X_train, y_train, batch_size=32), 
            epochs=10, steps_per_epoch=len(X_train) // 32, 
            validation_data=(X_val, y_val))

    model.evaluate(X_test, y_test)

    return model