from pathlib import Path
from models.nns import ConvolutionModel
import models.utils.image_processor as imp


if __name__ == '__main__':
    # Define paths
    logging_path = Path("logs")
    img_path = Path("sources")
    original_path = img_path.joinpath("original")
    processed_path = img_path.joinpath("processed")
    # Resize images
    imp.resize_images_in(original_path, processed_path, 256, 256)
    # Get new model
    # model = ConvolutionModel(processed_path, 3, 3)
