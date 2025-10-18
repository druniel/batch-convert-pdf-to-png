import re
import shutil
from pathlib import Path

# složka s hotovými PNG podadresáři
pngs_dir = Path("../slozky")

# složka s mp3 soubory
mp3_dir = Path("../nahravky")

# projdi všechny mp3
for mp3_file in mp3_dir.glob("*.mp3"):
    # najdi první trojmístné číslo v názvu mp3
    match = re.search(r"\d{3}", mp3_file.stem)
    if not match:
        print(f"⚠️ Přeskočeno (nenalezeno číslo): {mp3_file.name}")
        continue

    number = match.group()  # např. "123"

    # najdi odpovídající složku ve PNGs, která obsahuje to číslo
    candidates = [d for d in pngs_dir.iterdir() if d.is_dir() and number in d.name]

    if not candidates:
        print(f"❌ Nenašla se složka pro {mp3_file.name} (číslo {number})")
        continue

    if len(candidates) > 1:
        print(f"⚠️ Více složek odpovídá {number}: {candidates} – beru první")
    
    target_dir = candidates[0]
    target_path = target_dir / mp3_file.name

    # přesun mp3 do cílové složky
    shutil.move(str(mp3_file), target_path)
    print(f"✅ {mp3_file.name} -> {target_dir}")