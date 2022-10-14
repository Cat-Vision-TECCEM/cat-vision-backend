from pathlib import Path
from models.nns import ConvolutionModel
import models.utils.image_processor as imp


if __name__ == '__main__':
    # Define paths
    logging_path = Path("logs")
    img_path = Path("temp")
    original_path = img_path.joinpath("original")
    resized_path = img_path.joinpath("processed", "resized")
    grayscale_path = img_path.joinpath("processed", "bw")
    # Resize images
    imp.resize_images_in(original_path, resized_path, 256, 256)
    imp.to_grayscale(resized_path, grayscale_path)
    # Get new model
    # model = ConvolutionModel(processed_path, 3, 3)
