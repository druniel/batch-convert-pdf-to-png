import shutil
from pathlib import Path

# cesta ke složce s podadresáři
pngs_dir = Path("../slozky")

# cesta k jednomu PNG souboru, který chceš rozkopírovat
source_png = Path("../uvod.png")   # změň podle sebe

if not source_png.exists():
    raise FileNotFoundError(f"Soubor {source_png} neexistuje!")

# projdi všechny složky v PNGs
for folder in pngs_dir.iterdir():
    if folder.is_dir():
        target_file = folder / source_png.name
        shutil.copy2(source_png, target_file)
        print(f"✅ {source_png.name} -> {folder}")