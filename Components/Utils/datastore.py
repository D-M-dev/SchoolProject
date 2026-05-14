import json
import os

_SAVE_DIR = "data"
_stores = {}

def init():
    os.makedirs(_SAVE_DIR, exist_ok=True)


def get_store(name: str) -> "DataStore":
    if name not in _stores:
        _stores[name] = DataStore(name)
    return _stores[name]


class DataStore:
    def __init__(self, name: str):
        self._name = name
        self._path = os.path.join(_SAVE_DIR, f"{name}.json")
        self._cache: dict = {}
        self._load()

    def _load(self):
        if os.path.exists(self._path):
            with open(self._path, "r", encoding="utf-8") as f:
                self._cache = json.load(f)
        else:
            self._cache = {}

    def _save(self):
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump(self._cache, f, indent=2, ensure_ascii=False)

    def get(self, key: str, default=None):
        return self._cache.get(key, default)

    def set(self, key: str, value):
        self._cache[key] = value
        self._save()

    def update(self, key: str, updater):
        current = self._cache.get(key)
        self._cache[key] = updater(current)
        self._save()

    def remove(self, key: str):
        self._cache.pop(key, None)
        self._save()

    def wipe(self):
        self._cache = {}
        self._save()