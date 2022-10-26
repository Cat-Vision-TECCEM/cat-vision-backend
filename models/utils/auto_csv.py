from pathlib import Path

folder_path = Path("models").joinpath("temp")

with open(folder_path.joinpath("skus.csv"), "w+") as f:
    f.write("sku, name\n")
    for index, child in enumerate(Path("models/temp").rglob('*')):
        if child.is_dir():
            classname = ' '.join(child.name.split('_'))
            f.write(f"sku_{index:03d}, {classname}\n")
