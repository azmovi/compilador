import pytest

from compilador.exceptions import InvalidPath
from compilador.utils import get_file


def test_get_file():
    valid_path = 'tests/files/input/test1.la'

    file_path = get_file(valid_path)

    assert valid_path in file_path


def test_get_file_with_wrong_path():
    invalid_path = 'xpto'

    with pytest.raises(InvalidPath):
        get_file(invalid_path)


def test_get_file_with_wrong_extension(create_file):
    invalid_file = create_file('xpto')
    with pytest.raises(InvalidPath):
        get_file(invalid_file)
