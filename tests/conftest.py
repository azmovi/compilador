import pytest


@pytest.fixture
def create_file(tmp_path):
    def _create_file(name: str, content: str = 'conteúdo default'):
        file = tmp_path / name
        file.write_text(content)
        return file

    return _create_file
