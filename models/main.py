from pathlib import Path
from nns import Model
import utils.image_processor as imp


if __name__ == '__main__':
    # Define paths
    img_path = Path("models").joinpath("temp")
    # Image processing paths
    original_img_path = img_path.joinpath("ciel_600ml")
    processed_img_path = img_path.joinpath("temp_processed")
    # Model output path
    output_path = Path("models")
    # Resize images
    IMG_HEIGHT = 224
    IMG_WIDTH = 224
    imp.resize_images_recursive(original_img_path, processed_img_path, IMG_HEIGHT, IMG_WIDTH)
    # Get new model
    """ model = Model(processed_img_path, (IMG_HEIGHT, IMG_WIDTH))
    model.model.save(output_path, include_optimizer=True) """
