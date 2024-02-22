from keras.applications import VGG16
from keras.models import Sequential
from keras.layers import Conv2D, AveragePooling2D, Flatten, Dense, MaxPooling2D, Dropout
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
    model.add(Dense(128, activation='relu', kernel_regularizer=l2(0.01)))
    model.add(Dropout(0.5))
    model.add(Dense(NUM_CLASSES, activation='sigmoid'))

    # Compile the model
    model.compile(
        loss='binary_crossentropy',
        optimizer=RMSprop(learning_rate=1e-5),
        metrics=['accuracy']
    )

    # Display the model structure
    model.summary()

    # Create a data generator for the data augmentation
    datagen = ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.05,
        height_shift_range=0.05,
        shear_range=0.05,
        brightness_range=[0.1, 1.5],
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