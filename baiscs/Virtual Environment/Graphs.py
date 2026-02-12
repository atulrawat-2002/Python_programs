import csv
import os 
from collections import defaultdict
import matplotlib.pyplot as plt


FILENAME = "Sample_data.csv"


def visualize_weather():

    dates = []
    temps = []
    conditions = defaultdict(int)

    with open(FILENAME, "r", encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            dates.append(row["Date"])
            temps.append(row['Temperature'])
            conditions[row['Condition']] += 1
    if not dates:
        print("No data available ")
        return

    plt.figure(figsize=(6, 3))
    plt.plot(dates, temps, marker='o')
    plt.title("Temperaure over Time ")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(4, 2))
    plt.bar(conditions.keys(), conditions.values(), color='skyblue')
    plt.xlabel("Conditions")
    plt.ylabel("Days")
    plt.show()


visualize_weather()