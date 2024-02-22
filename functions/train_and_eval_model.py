from keras.applications import VGG16
from keras.models import Sequential
from keras.layers import Dense, Flatten, BatchNormalization, Dropout
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator

def train_and_eval_model(X_train, y_train, X_val, y_val, X_test, y_test):
    # Créer un modèle VGG-16 pré-entraîné (ne pas inclure la couche dense finale)
    base_model = VGG16(input_shape=(32,32,3), include_top=False)

    NUM_CLASSES = 10

    model = Sequential()
    model.add(base_model)
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(NUM_CLASSES, activation='sigmoid'))

    # figer les poids du VGG
    model.layers[0].trainable = False

    # Compiler le modèle
    model.compile(
        loss='binary_crossentropy',
        optimizer=RMSprop(lr=1e-4),
        metrics=['accuracy']
    )

    # Afficher la structure du modèle
    model.summary()

    # Créer un générateur d'images pour la data augmentation
    datagen = ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.05,
        height_shift_range=0.05,
        rescale=1./255,
        shear_range=0.05,
        brightness_range=[0.1, 1.5],
        horizontal_flip=True,
        vertical_flip=True
    )

    # Ajuster le générateur aux données d'entraînement
    datagen.fit(X_train)

    # Entraîner le modèle avec l'augmentation de données
    model.fit(datagen.flow(X_train, y_train, batch_size=32), 
            epochs=10, steps_per_epoch=len(X_train) // 32, 
            validation_data=(X_val, y_val))

    model.evaluate(X_test, y_test)