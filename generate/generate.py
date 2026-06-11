import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["Напиток", "Объем", "Цена", "Сироп"]

def generate_row():

    return {
        "Напиток": random.choice(["Латте", "Капучино", "Эспрессо", "Раф"]),
        "Объем": random.choice([0.2, 0.3, 0.4, 0.6]),
        "Цена": random.randint(150, 500),
        "Сироп": random.choice(["Шоколадный", "Ореховый", "Соленая карамель", "Ванильный"]),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)