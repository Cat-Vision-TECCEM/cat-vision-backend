import os
from pathlib import Path
import random
import utils.file_handler as fh

def split_data(source_dir: str | Path, output_dir: str | Path):
    source_dir = fh.to_path(source_dir) 
    output_dir = fh.to_path(output_dir)
    fh.copy_subdirs_from(source_dir, output_dir)

    for child in source_dir.rglob('*'):
        if child.is_dir():
            files = os.listdir(child)
            limit = int(len(files) * 0.8)
            while len(files) > limit:
                random_file = source_dir.joinpath(child.name, files.pop(random.randint(0, len(files) - 1)))
                output_path = output_dir.joinpath(child.name, random_file.name)
                os.rename(fh.to_str(random_file), fh.to_str(output_path))