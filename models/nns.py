import numpy as np
import tensorflow as tf
from pathlib import Path
from tensorflow import keras
from utils.misc import default
from utils.files.file_handler import PathHandler


class ConvolutionModel:

    def __init__(self, dataset_path: str | Path, checkpoint_path: str | Path, conv_layers: int, dense_layers: int, image_size: tuple) -> None:
        self.__data_path = PathHandler.to_path(dataset_path)
        self.__ckpt_path = PathHandler.to_path(checkpoint_path)
        self.__image_size = image_size
        self.__train_data, self.__validation_data = ConvolutionModel.__get_split_data(self.__data_path, self.__image_size)
        self.classes = PathHandler.get_subdir_names_from(dataset_path)
        self.model = self.__get_model(len(self.classes), conv_layers, dense_layers)

    @staticmethod
    def __get_split_data(data_path: str or Path, image_size: tuple):
        train_data = keras.utils.image_dataset_from_directory(data_path, validation_split=0.2, subset='training', seed=123, image_size=image_size)
        validation_data = keras.utils.image_dataset_from_directory(data_path, validation_split=0.2, subset='training', seed=123, image_size=image_size)
        train_data.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)
        validation_data.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)
        return train_data, validation_data

    def __get_model(self, num_classes: int, convolution_layers: int, dense_layers: int, rescaling: bool = True, augmentation: bool = True, dropout: bool = False, dropout_rate: float = 0.2) -> keras.Sequential:
        # Avoid errors
        convolution_layers = default(convolution_layers, 1)
        dense_layers = default(dense_layers, 1)
        # Generate list of layers
        sequential_layers = []
        if rescaling:
            sequential_layers.append(keras.layers.Rescaling(1./255, input_shape=(256, 256, 3)))
        if augmentation:
            sequential_layers.append(keras.Sequential([
                keras.layers.RandomFlip(mode='horizontal', input_shape=(256, 256, 3)),
                keras.layers.RandomBrightness(0.15)
            ]))
        for n in range(convolution_layers):
            sequential_layers.append(keras.layers.Conv2D(16 * (n + 1), 3, padding='same', activation='relu'))
            sequential_layers.append(keras.layers.MaxPooling2D())
        if dropout:
            sequential_layers.append(keras.layers.Dropout(dropout_rate))
        sequential_layers.append(keras.layers.Flatten())
        for n in range(dense_layers):
            if n + 1 == dense_layers:
                sequential_layers.append(keras.layers.Dense(num_classes))
            else:
                sequential_layers.append(keras.layers.Dense(2 ** (dense_layers - n) + 3))
        model = keras.Sequential(sequential_layers)
        model.compile(optimizer='adam', loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
        model.save_weights(PathHandler.to_str(self.__ckpt_path).format(epoch=0))
        return model

    def get_callbacks(self, batch_size: int) -> keras.callbacks.ModelCheckpoint:
        return keras.callbacks.ModelCheckpoint(filepath=self.__ckpt_path, save_weights_only=True, save_freq=batch_size, verbose=0)

    def train_model(self, epochs, batch_size=5, details=False):
        callbacks = self.get_callbacks(batch_size)
        history = self.model.fit(self.__train_data, epochs=epochs, validation_data=self.__validation_data, batch_size=batch_size, callbacks=[callbacks], verbose=0)
        if details:
            return tf.train.latest_checkpoint(self.__ckpt_path), history
        return tf.train.latest_checkpoint(self.__ckpt_path)

    def predict_image(self, image_path: str or Path):
        image = keras.utils.load_img(PathHandler.to_path(image_path), target_size=self.__image_size)
        image_array = tf.expand_dims(keras.utils.img_to_array(image), 0)
        predictions = self.model.predict(image_array)
        score = tf.nn.softmax(predictions[0])
        return self.classes[np.argmax(score)], 100 * np.max(score)


