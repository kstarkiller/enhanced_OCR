from keras.applications import VGG16
from keras.models import Sequential
from keras.layers import Flatten, Dense, Dropout
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator

NUM_CLASSES = 10

def negative_image(image):
    image = image * 255 # Avoid scaling
    return 1.0 - image / 255 # Invert the colors and rescale

def train_and_eval_VGG(X_train, y_train, X_val, y_val, X_test, y_test):
    # Create a pre-trained VGG-16 model (do not include the final dense layer)
    base_model = VGG16(input_shape=(32,32,1), include_top=False)

    model = Sequential()
    model.add(base_model)
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(NUM_CLASSES, activation='softmax'))

    # Fine-tuning
    for layer in base_model.layers:
        layer.trainable = True

    # Compile the model
    model.compile(
        loss='categorical_crossentropy',
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
        rescale=1./255,
        shear_range=0.05,
        brightness_range=[0.1, 1.5],
        horizontal_flip=True,
        vertical_flip=True,
        channel_shift_range=0.5,
        preprocessing_function=negative_image
    )


    # Adjust the generator to the training data
    datagen.fit(X_train)

    # Train the model with data augmentation
    model.fit(datagen.flow(X_train, y_train, batch_size=32), 
            epochs=10, steps_per_epoch=len(X_train) // 32, 
            validation_data=(X_val, y_val))

    model.evaluate(X_test, y_test)

    return model