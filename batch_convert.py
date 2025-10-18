import os
from pathlib import Path
from pdf2image import convert_from_path
from multiprocessing import Pool, cpu_count

# složka se všemi PDF
input_dir = Path("../noty")
output_dir = Path("../slozky")
output_dir.mkdir(exist_ok=True)

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

if __name__ == "__main__":
    pdf_files = list(input_dir.glob("*.pdf"))
    print(f"Načteno {len(pdf_files)} PDF souborů")

    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_pdf, pdf_files)

    print("\n".join(results))
    print("✅ Vše hotovo!")