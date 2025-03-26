import json

def save_to_json(data, filename="../output/results.json"):
    """Save extracted tasks to JSON."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
