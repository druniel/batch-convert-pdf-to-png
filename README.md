# Batch Convert PDF to PNG and two other small programs

Small collection of utilities. The main one is for converting PDF files to PNG images. The two smaller ones are for moving mp3 and png files through directories. All is done using Python. I only focus on the PDF to PNG convert utlity in this Readme.

## Features
- Batch convert all PDFs in a selected folder into PNG images (one folder per PDF).
- Simple GUI prompts for input and output folders (Tkinter).
- Parallel processing using multiprocessing.
- Progress display with tqdm.

## Requirements
- Python 3.8+
- pip packages:
  - pdf2image
  - pillow
  - tqdm
- Poppler (system dependency required by pdf2image)
- Tkinter (usually included with standard Python on Windows)

Example requirements (requirements.txt):
```
pdf2image
pillow
tqdm
```

## Installation
1. Create and activate a virtual environment (recommended):
   - Windows (PowerShell):
     ```
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - Windows (cmd):
     ```
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install Poppler for Windows and ensure the `bin` folder is on your PATH (pdf2image requires poppler utilities).

## Usage
Run the main script and follow the folder selection dialogs:
```
python batch_convert.py
```
- Select the input folder containing `.pdf` files.
- Select an output folder where PNG folders will be created.
- The script will convert each PDF into PNG files (one PNG per page) and show progress.

## Notes
- Output DPI is set to 300 in the script; change this value in `batch_convert.py` if needed.
- The script creates one subfolder per PDF named after the PDF file (without extension).
- For large PDFs or many files, ensure sufficient disk space and consider adjusting process count.
