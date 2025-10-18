import shutil
from pathlib import Path

# path
pngs_dir = Path("../slozky")

# path for the png file which will be copied
source_png = Path("../uvod.png")

if not source_png.exists():
    raise FileNotFoundError(f"Soubor {source_png} neexistuje!")

# copy to all folders in path
for folder in pngs_dir.iterdir():
    if folder.is_dir():
        target_file = folder / source_png.name
        shutil.copy2(source_png, target_file)
        print(f"{source_png.name} -> {folder}")