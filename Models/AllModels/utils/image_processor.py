import random
import cv2
import numpy as np
from pathlib import Path
import utils.file_handler as fh


def resize_image(image_path: str | Path, output_path: str | Path, height: int, width: int) -> None:
    original = cv2.imread(fh.to_str(image_path), cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(original, (width, height), interpolation=cv2.INTER_AREA)
    cv2.imwrite(fh.to_str(output_path), resized)


def resize_images_recursive(source_dir: str | Path, output_dir: str | Path, height: int, width: int) -> None:
    source_path = fh.to_path(source_dir)
    output_parent = fh.to_path(output_dir)
    fh.copy_subdirs_from(source_dir, output_dir)
    for child in source_path.rglob('*'):
        if child.is_file():
            output_path = output_parent.joinpath(child.parent.name, child.name)
            resize_image(child, output_path, height, width)


def resize_images_in(source_dir: str | Path, output_dir: str | Path, height: int, width: int) -> None:
    source_path = fh.to_path(source_dir)
    output_parent = fh.to_path(output_dir)
    fh.copy_subdirs_from(source_dir, output_dir)
    for child in source_path.rglob('*'):
        if child.is_file():
            output_path = output_parent.joinpath(child.parent.name, child.name)
            resize_image(child, output_path, height, width)


def modify_contrast(image) -> np.uint8:
    contrast = random.randint(1, 20)
    brightness = 10
    dummy = np.int16(image)
    dummy = dummy * (contrast / 127 + 1) - contrast + brightness
    dummy = np.clip(dummy, 0, 255)
    new_image = np.uint8(dummy)
    return new_image


def modify_single_hsv(hsv_val, alteration_value: int):
    if alteration_value >= 0:
        limit = 255 - alteration_value
        hsv_val[hsv_val > limit] = 255
        hsv_val[hsv_val <= limit] += alteration_value
    else:
        limit = np.absolute(alteration_value)
        hsv_val[hsv_val < limit] = 255
        hsv_val[hsv_val >= limit] -= np.absolute(alteration_value)
    return hsv_val

def modify_hsv(values, alteration_value: int):
    h, s, v = cv2.split(values)
    s = modify_single_hsv(s, alteration_value)
    v = modify_single_hsv(v, alteration_value)
    final_hsv = cv2.merge((h, s, v))
    return final_hsv


def color_jitter_dir(source_dir: str | Path, output_dir: str | Path) -> None:
    source_dir = fh.to_path(source_dir)
    for child in source_dir.rglob('*'):
        if child.is_file():
            output_name = f"{child.with_suffix('').name}_cjit{child.suffix}"
            output_path = fh.to_path(output_dir).joinpath(child.parent.name, output_name)
            image = cv2.imread(fh.to_str(child))
            alteration_value = np.random.choice(np.array([-10, -8, -5, 5, 8, 10]))
            hsv_values = modify_hsv(cv2.cvtColor(image, cv2.COLOR_BGR2HSV), alteration_value)
            new_image = cv2.cvtColor(hsv_values, cv2.COLOR_HSV2BGR)
            new_image = modify_contrast(new_image)
            cv2.imwrite(fh.to_str(output_path), new_image)
