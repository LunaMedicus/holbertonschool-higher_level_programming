#!/usr/bin/python3
"""CSV to JSON conversion helpers."""
import csv
import json


def convert_csv_to_json(filename):
    """Convert CSV data from a file into JSON data.json."""
    try:
        with open(filename, encoding="utf-8") as csv_file:
            rows = list(csv.DictReader(csv_file))

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(rows, json_file)
        return True
    except FileNotFoundError:
        return False
