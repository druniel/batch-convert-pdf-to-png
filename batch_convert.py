import os
from pathlib import Path
from pdf2image import convert_from_path
from multiprocessing import Pool, cpu_count
import tkinter as tk
from tkinter import filedialog, messagebox
from tqdm import tqdm
import sys

root = tk.Tk()
root.withdraw()

# function for path selection dialog
def vyber_slozku(popis):
    while True:
        cesta = filedialog.askdirectory(title=popis)

        if cesta:
            return cesta
        else:
            volba = messagebox.askyesno("Nebyla vybrána složka", "Chcete složku vybrat znovu?")
            if not volba:
                print("Program ukončen.")
                sys.exit(0)

# paths
input_path = vyber_slozku("Vyberte vstupní složku")
output_path = vyber_slozku("Vyberte výstupní složku")

input_dir = Path(input_path)
output_dir = Path(output_path)
output_dir.mkdir(exist_ok=True)

# function to convert pdfs to pngs
def process_pdf(pdf_file: Path):
    pdf_name = pdf_file.stem
    pdf_out_dir = output_dir / pdf_name
    pdf_out_dir.mkdir(exist_ok=True)

    try:
        pages = convert_from_path(pdf_file, dpi=300)
        for i, page in enumerate(pages, start=1):
            out_path = pdf_out_dir / f"{pdf_name}_page{i}.png"
            page.save(out_path, "PNG")
        return f"Hotovo: {pdf_file.name} ({len(pages)} stránek)"
    except Exception as e:
        return f"Chyba: {pdf_file.name} ({e})"

# main logic
if __name__ == "__main__":
    pdf_files = list(input_dir.glob("*.pdf"))
    print(f"Načteno {len(pdf_files)} PDF souborů")

    with Pool(processes=cpu_count()) as pool:
        results = list(tqdm(pool.imap(process_pdf, pdf_files), total=len(pdf_files), desc="Zpracování PDF"))

    print("\n".join(results))
    print("Vše hotovo!")

root.destroy()