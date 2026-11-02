"""Handy Python utility helpers."""

import os
import json
from datetime import datetime


def read_json(path):
    """Read and parse a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data, indent=2):
    """Write data to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def now_str(fmt="%Y-%m-%d %H:%M:%S"):
    """Return current time as formatted string."""
    return datetime.now().strftime(fmt)


def ensure_dir(path):
    """Create directory if it does not exist."""
    os.makedirs(path, exist_ok=True)
    return path


if __name__ == "__main__":
    print("Utilities loaded. Current time:", now_str())
