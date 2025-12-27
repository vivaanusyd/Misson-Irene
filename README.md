Folder Name Obfuscator
A Python script that renames folders to random names and writes a log so the original names can be restored later.
It works with any directory structure and does not assume specific folder names or depth.
What it does
Walks through a directory recursively
Renames every folder to a random name
Creates a log of each rename
Restores original folder names using the log
Only folder names are changed. Files are not touched.
Example
Before:
HONOURS_testing/
├── Victoria/
│   ├── Rear/
│   │   └── Day/
After:
HONOURS_testing/
├── Pikachu/
│   ├── Bulbasaur/
│   │   └── Charmander/
Log file
A file called log.txt is created in the root directory.
Each rename is stored as:
/full/path/to/original
=
/full/path/to/renamed
This log is used to restore the original folder names.
How to use
Requirements
Python 3
A CSV file containing names to use (one name per line)
Setup
Edit these values at the top of the script:
ROOT_DIR = "/path/to/your/folder"
POKEMON_CSV = "pokemon.csv"
Encode (rename folders)
python obfuscate.py
If no log exists, folders will be renamed and a log will be created.
Decode (restore original names)
Run the script again.
If a log is found, you’ll be asked whether to restore the original names.
