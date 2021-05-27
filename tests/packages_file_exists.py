import pytest
import os

PACKAGES_FILENAME = "packages.json"
BASE_DIR = os.path.dirname(__file__)

def test_packages_file_exists():
    assert os.path.exists(os.path.join(BASE_DIR, PACKAGES_FILENAME)) == True
