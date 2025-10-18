import re
import shutil
from pathlib import Path

# path
pngs_dir = Path("../slozky")

# folder with mp3s
mp3_dir = Path("../nahravky")

# go through all mp3s
for mp3_file in mp3_dir.glob("*.mp3"):
    # find first 3 figure number in name of mp3
    match = re.search(r"\d{3}", mp3_file.stem)
    if not match:
        print(f"Přeskočeno (nenalezeno číslo): {mp3_file.name}")
        continue
    number = match.group()

    # find a folder in path, which has the same number
    candidates = [d for d in pngs_dir.iterdir() if d.is_dir() and number in d.name]

    if not candidates:
        print(f"Nenašla se složka pro {mp3_file.name} (číslo {number})")
        continue

    # take the first matching folder if there are more
    if len(candidates) > 1:
        print(f"Více složek odpovídá {number}: {candidates} – beru první")
    target_dir = candidates[0]
    target_path = target_dir / mp3_file.name

    # move mp3 to path
    shutil.move(str(mp3_file), target_path)
    print(f"{mp3_file.name} -> {target_dir}")