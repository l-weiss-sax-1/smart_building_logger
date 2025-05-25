import json
import os
import random

class LocalStorage:
    def __init__(self, directory="data"):
        os.makedirs(directory, exist_ok=True)
        self.directory = directory

    def save(self, filename, data):
        path = os.path.join(self.directory, filename)
        try:
            with open(path, "w") as f:
                json.dump(data, f)
        except Exception as e:
            raise

    def load(self, filename):
        path = os.path.join(self.directory, filename)
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return None
