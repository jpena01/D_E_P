import json
import os

DATA_DIR = "data"
DATA_PATH = "data/tasks.json"

def load_tasks():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_PATH, "w") as f:
        json.dump(tasks, f, indent=4)
