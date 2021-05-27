import pytest
from pathlib import Path
import os

PACKAGES_FILENAME = "packages.json"
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

def test_packages_file_exists():
    assert os.path.exists(os.path.join(BASE_DIR, PACKAGES_FILENAME)) == True
