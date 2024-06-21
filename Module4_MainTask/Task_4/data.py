import json
import os


def load_contacts(filepath):
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        return {}
    with open(filepath, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_contacts(filepath, contacts):
    with open(filepath, 'w') as file:
        json.dump(contacts, file)