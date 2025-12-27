import os
import csv
import random
import sys

# ================= CONFIG =================
ROOT_DIR = "/Volumes/Extreme Pro/HONOURS_testing"
LOG_PATH = os.path.join(ROOT_DIR, "log.txt")
POKEMON_CSV = "pokemon.csv"
# ==========================================


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


def load_pokemon_names():
    names = []
    with open(POKEMON_CSV, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row:
                names.append(row[0])
    return names


def get_random_name(names, used):
    available = list(set(names) - used)
    if not available:
        raise RuntimeError("Ran out of Pokémon names!")
    choice = random.choice(available)
    used.add(choice)
    return choice


def walk_dirs_bottom_up(root):
    """Yield all directories bottom-up"""
    for current, dirs, _ in os.walk(root, topdown=False):
        for d in dirs:
            yield os.path.join(current, d)


def decode():
    print("Decoding from log...\n")

    with open(LOG_PATH) as f:
        blocks = f.read().strip().split("\n\n")

    # Reverse order is critical
    for block in reversed(blocks):
        original, encoded = block.split("\n=\n")

        if os.path.exists(encoded):
            os.rename(encoded, original)

    print("Decoding completed.")
    sys.exit(0)


def encode():
    names = load_pokemon_names()
    used = set()

    with open(LOG_PATH, "w") as log:
        for dir_path in walk_dirs_bottom_up(ROOT_DIR):

            parent = os.path.dirname(dir_path)
            original_name = os.path.basename(dir_path)

            new_name = get_random_name(names, used)
            new_path = os.path.join(parent, new_name)

            log.write(f"{dir_path}\n=\n{new_path}\n\n")
            os.rename(dir_path, new_path)

    print("Encoding completed.")


# ================= MAIN =================
clear()
print("Checking directories...")

if os.path.exists(LOG_PATH) and os.path.getsize(LOG_PATH) > 0:
    ans = input("Folder already encoded. Decode it? (y/n): ").lower()
    if ans == "y":
        decode()
    else:
        print("Aborted.")
        sys.exit(0)

encode()
