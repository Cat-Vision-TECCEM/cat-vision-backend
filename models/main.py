from pathlib import Path
from nns import Model
from matplotlib import pyplot as plt
import utils.image_processor as imp
from utils.train_test_split import split_data


if __name__ == '__main__':
    # Define paths
    img_path = Path("models")
    # Image processing paths
    original_img_path = img_path.joinpath("temp")
    processed_img_path = img_path.joinpath("temp_processed")
    # Training path and validation path
    train_path = processed_img_path.joinpath("training")
    validation_path = processed_img_path.joinpath("validation")
    # Model output path
    output_path = Path("models")
    checkpoint_path = output_path.joinpath("checkpoints")
    # Resize images
    IMG_HEIGHT = 224
    IMG_WIDTH = 224
    # imp.resize_images_recursive(processed_img_path, processed_img_path, IMG_HEIGHT, IMG_WIDTH)
    # imp.color_jitter_dir(original_img_path, processed_img_path)
    # Get new model
    # split_data(train_path, validation_path)
    model = Model(processed_img_path, (IMG_HEIGHT, IMG_WIDTH))
    history = model.train_model(10)
    # Plot accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model Accuracy')
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()
    # Save model
    model.model.save(output_path, include_optimizer=True)

