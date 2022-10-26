import os
from pathlib import Path


folder_path = Path("models").joinpath("temp")

for index, child in enumerate(Path("models/temp_processed/training").rglob('*')):
    if child.is_dir():
        classname = f"sku_{index:03d}"
        new_name = child.parent.joinpath(classname)
        os.rename(str(child), new_name)
        print(str(child), new_name)
