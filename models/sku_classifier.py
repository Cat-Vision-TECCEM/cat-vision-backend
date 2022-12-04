import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow import keras
from pathlib import Path
from nns import Model
import utils.image_processor as imp
from utils.train_test_split import split_data


if __name__ == '__main__':
    # Define paths
    img_path = Path("models")
    # Image processing paths
    original_img_path = Path.cwd().joinpath("models", "data", "unknown_classification")
    processed_img_path = Path.cwd().joinpath("models", "temp_processed")
    # Training path and validation path
    train_path = processed_img_path.joinpath("training")
    validation_path = processed_img_path.joinpath("validation")
    # Model output path
    output_path = Path("models").joinpath("saved")
    checkpoint_path = output_path.joinpath("checkpoints")
    # Resize images
    IMG_HEIGHT = 224
    IMG_WIDTH = 224
    imp.resize_images_recursive(original_img_path, processed_img_path, IMG_HEIGHT, IMG_WIDTH)
    imp.color_jitter_dir(original_img_path, processed_img_path)
    # Get new model
    # split_data(train_path, validation_path)
    """ model = Model(processed_img_path.absolute(), (IMG_HEIGHT, IMG_WIDTH))
    training_labels = model.training_labels
    history = model.train_model(15, output_path.joinpath("sku_classifier.h5"))
    # Load model
    model_path = output_path.joinpath("sku_classifier.h5")
    model = keras.models.load_model(model_path) """
