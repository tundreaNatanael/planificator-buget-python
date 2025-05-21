import pandas as pd
import csv
from datetime import datetime

class CVS:
    CVS_FILE = "date_intrare.csv"
    COLUMNS = ["categorie", "optiune"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CVS_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CVS_FILE, index=False)

    @classmethod
    def add_entry(cls, categorie, optiune):
        new_entry = {
            "categorie": categorie,
            "optiune": optiune,
        }
        with open(cls.CVS_FILE, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")

    @classmethod
    def read_entries(cls):
        try:
            df = pd.read_csv(cls.CVS_FILE)
            return df.to_dict(orient="records")
        except FileNotFoundError:
            print("CSV file not found.")
            return []

    @classmethod
    def write_entry(cls, categorie, optiune):
        cls.add_entry(categorie, optiune)

    @classmethod
    def write_buget(self, results):
        output_file = "buget_generat.csv"
        columns = ["categorie", "valoare"]
        with open(output_file, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            writer.writerows(results)
        print(f"Rezultatele au fost scrise in {output_file}")
