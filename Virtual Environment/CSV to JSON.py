import json
import csv
import os

INPUT_FILE = "Sample_data.csv"
OUTPUT_FILE = "result.json"

def load_data(filename):

    if not os.path.exists(filename):
        print("CSV file not found!")    
        return []
    
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        return data
    
def convert_data(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


data = load_data(INPUT_FILE)
convert_data(data, OUTPUT_FILE)