from keras.applications import VGG16
from keras.models import Sequential
from keras.layers import Conv2D, Flatten, Dense, MaxPooling2D, Dropout, BatchNormalization
from keras.regularizers import l2
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator

NUM_CLASSES = 10

def train_and_eval_CNN(X_train, y_train, X_val, y_val, X_test, y_test):
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(5,5), activation='relu', input_shape=(32,32,1)))
    model.add(Conv2D(32, (5,5), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation='softmax'))

    # Compile the model
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    # Display the model structure
    model.summary()

    # # Create a data generator for the data augmentation
    # datagen = ImageDataGenerator(
    #     rotation_range=10,  # rotation aléatoire des images dans la plage (degrés, 0 à 180)
    #     zoom_range = 0.1, # Zoom aléatoire 
    #     width_shift_range=0.1,  # décalage aléatoire horizontal des images (fraction totale de la largeur)
    #     height_shift_range=0.1,  # décalage aléatoire vertical des images (fraction totale de la hauteur)
    # )

    # Adjust the generator to the training data
    # datagen.fit(X_train)

    # Train the model with data augmentation
    model.fit(X_train, y_train, batch_size=64,
                epochs=10,
                validation_data=(X_val, y_val)
            )

    model.evaluate(X_test, y_test)

    return model