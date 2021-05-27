import pytest
from pathlib import Path
import json
import os

PACKAGES_FILENAME = "packages.json"
BASE_DIR = Path(__file__).resolve().parent.parent
PACKAGES_FULLPATH = os.path.join(BASE_DIR, PACKAGES_FILENAME)


def test_packages_file_exists():
    assert os.path.exists(PACKAGES_FULLPATH) is True


def test_packages_access():
    with open(PACKAGES_FULLPATH, "r") as file:
        source = json.load(file)
        assert source["packages"][0] == "atom-beautify"
