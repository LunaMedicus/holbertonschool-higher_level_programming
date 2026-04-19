#!/usr/bin/python3
"""Basic JSON serialization helpers."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load a dictionary from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
