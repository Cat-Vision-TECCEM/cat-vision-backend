import numpy as np
import tensorflow as tf
from pathlib import Path
from tensorflow import keras
from keras import layers
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.inception_v3 import InceptionV3
from keras.applications.vgg16 import VGG16
from keras.applications import Xception
from keras.optimizers import RMSprop, Adam
import utils.file_handler as fh


class Model:

    def __init__(self, dataset_path: str | Path, image_size: tuple) -> None:
        self.__data_path = fh.to_path(dataset_path)
        self.__image_size = image_size
        self.__train_path = self.__data_path.joinpath("training")
        self.__validation_path = self.__data_path.joinpath("validation")
        self.__train_data, self.__test_data = self.__generate_data(self.__train_path, self.__validation_path, image_size)
        self.classes = fh.get_subdir_names_from(self.__train_path)
        self.model = self.__get_model((image_size[0], image_size[1], 3))

    @staticmethod
    def __generate_data(train_path: str | Path, val_path: str | Path, image_size: tuple):
        # Create ImageDataGenerators for the images
        train_gen = ImageDataGenerator(rescale=1./255.)
        test_gen = ImageDataGenerator(rescale=1./255.)
        # Create processed and validation data
        train_data = train_gen.flow_from_directory(train_path, batch_size=10, class_mode='categorical', target_size=image_size)
        validation_data = test_gen.flow_from_directory(val_path, batch_size=10, class_mode='categorical', target_size=image_size)
        return train_data, validation_data

    def __get_model(self, input_shape: tuple[int]) -> keras.Sequential:
        model = VGG16(include_top=False, input_shape=input_shape, weights='imagenet', classifier_activation='softmax')
        for layer in model.layers:
            layer.trainable = False
        non_trainable = layers.Flatten()(model.output)
        non_trainable = layers.Dense(1024, activation='relu')(non_trainable)
        non_trainable = layers.Dropout(0.2)(non_trainable)
        non_trainable = layers.Dense(len(self.classes), activation='softmax')(non_trainable)
        model = keras.models.Model(model.input, non_trainable)
        model.compile(optimizer=Adam(learning_rate=0.01), loss=keras.losses.CategoricalCrossentropy(from_logits=True), metrics=['acc'])
        print(model.summary())
        return model

    def train_model(self, epochs: int):
        history = self.model.fit(self.__train_data, validation_data=self.__test_data, steps_per_epoch=50, epochs=epochs)
        return history

    def predict_image(self, image_path: str | Path):
        image = keras.utils.load_img(fh.to_path(image_path), target_size=self.__image_size)
        image_array = tf.expand_dims(keras.utils.img_to_array(image), 0)
        predictions = self.model.predict(image_array)
        score = tf.nn.softmax(predictions[0])
        return self.classes[np.argmax(score)], 100 * np.max(score)
