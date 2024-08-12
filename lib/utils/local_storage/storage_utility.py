import json
import os

class LocalStorage:
    def __init__(self, filename='local_storage.json'):
        self.filename = filename
        # Load existing data
        self._load()

    def _load(self):
        """Load data from the file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self._data = json.load(file)
        else:
            self._data = {}

    def _save(self):
        """Save data to the file"""
        with open(self.filename, 'w') as file:
            json.dump(self._data, file)

    def save_data(self, key: str, value) -> None:
        """Save data to storage"""
        self._data[key] = value
        self._save()

    def read_data(self, key: str):
        """Read data from storage"""
        return self._data.get(key, None)

    def remove_data(self, key: str) -> None:
        """Remove data from storage"""
        if key in self._data:
            del self._data[key]
            self._save()

    def clear_all(self) -> None:
        """Clear all data in storage"""
        self._data = {}
        self._save()

# Example usage
if __name__ == '__main__':
    local_storage = LocalStorage()

    # Save data
    local_storage.save_data('username', 'JohnDoe')

    # Read data
    username = local_storage.read_data('username')
    print(f'Username: {username}')  # Output: Username: JohnDoe

    # Remove data
    local_storage.remove_data('username')

    # Clear all data
    local_storage.clear_all()
