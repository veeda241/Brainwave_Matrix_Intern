import json

# Load user data from JSON file
def load_data():
    try:
        with open('database.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save updated user data to JSON file
def save_data(data):
    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4)
