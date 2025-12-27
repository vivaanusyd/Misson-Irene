# Folder Name Obfuscator

A Python script that renames folders to random names and writes a log so the original names can be restored later.

It works with any directory structure and does not assume specific folder names or depth.

---

## What it does

- Walks through a directory recursively  
- Renames every folder to a random name  
- Creates a log of each rename  
- Restores original folder names using the log  

Only folder names are changed. Files are not touched.

---

## Log file

A file called `log.txt` is created automatically.

This log is used to restore the original folder names.
How to use
Requirements
Python 3
A CSV file containing names to use (one name per line)
Setup
Edit these values at the top of the script:ROOT_DIR = "/path/to/your/folder"
POKEMON_CSV = "pokemon.csv"
Encode (rename folders)
python obfuscate.py
If no log exists, folders will be renamed and a log will be created.
Decode (restore original names)
Run the script again.
If a log is found, the script will ask whether to restore the original names.
