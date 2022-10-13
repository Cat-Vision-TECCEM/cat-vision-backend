from PIL import Image
from pathlib import Path
from models.utils.file_handler import PathHandler

__handler = PathHandler()


def rgb_to_hsv(image_path: str | Path, output_path: str):
    pass


def resize_image(image_path: str | Path, output_path: str | Path, height: int, width: int, rotation: int = 0):
    original = Image.open(image_path).rotate(rotation, Image.NEAREST, expand=True if rotation != 0 else False)
    original.thumbnail((height, width))
    original.save(output_path)


def resize_images_in(source_dir: str | Path, output_dir: str | Path, height: int, width: int, rotation: int = 0):
    source_path = __handler.to_path(source_dir)
    output_parent = __handler.to_path(output_dir)
    __handler.copy_subdirs_from(source_dir, output_dir)
    for child in source_path.rglob('*'):
        if child.is_file():
            output_path = output_parent.joinpath(child.parent.name, child.name)
            resize_image(child, output_path, height, width, rotation=rotation)
