from PIL import Image, ImageOps
from pathlib import Path
import models.utils.file_handler as fh


def to_grayscale(source_dir: str | Path, output_dir: str | Path, suffix: str = '_bw') -> None:
    source_dir = fh.to_path(source_dir)
    output_dir = fh.to_path(output_dir)
    fh.copy_subdirs_from(source_dir, output_dir)
    for child in source_dir.rglob('*'):
        if child.is_file():
            output_path = output_dir.joinpath(child.parent.name, child.with_suffix('').name + suffix + child.suffix)
            image = Image.open(child)
            image = ImageOps.grayscale(image)
            image.save(output_path)


def resize_image(image_path: str | Path, output_path: str | Path, height: int, width: int, rotation: int = 0) -> None:
    original = Image.open(image_path).rotate(rotation, Image.NEAREST, expand=True if rotation != 0 else False)
    original.thumbnail((height, width))
    original.save(output_path)


def resize_images_in(source_dir: str | Path, output_dir: str | Path, height: int, width: int, rotation: int = 0) -> None:
    source_path = fh.to_path(source_dir)
    output_parent = fh.to_path(output_dir)
    fh.copy_subdirs_from(source_dir, output_dir)
    for child in source_path.rglob('*'):
        if child.is_file():
            output_path = output_parent.joinpath(child.parent.name, child.name)
            resize_image(child, output_path, height, width, rotation=rotation)