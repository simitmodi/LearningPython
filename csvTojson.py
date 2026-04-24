import csv
import json

def csv_to_json(csv_path, json_path):
    data = []

    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"JSON file created at: {json_path}")

# Example usage
csv_to_json("hospital_directory.csv", "hospital_data.json")
