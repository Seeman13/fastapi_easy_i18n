import json
import pytest

from fastapi_easy_i18n.translate import I18N_PATHS, __load_file, set_path


@pytest.fixture(autouse=True)
def reset_paths(tmp_path):
    original_paths = I18N_PATHS.copy()
    I18N_PATHS[:] = [str(tmp_path)]

    yield

    I18N_PATHS.clear()
    I18N_PATHS.extend(original_paths)


def test_load_file():
    assert __load_file('en', 'missing') == {}


def test_load_file_empty(tmp_path):
    folder = tmp_path.joinpath('en')
    folder.mkdir()
    folder.joinpath('empty.json').write_text('')

    assert __load_file('en', 'empty') == {}


def test_load_file_valid(tmp_path):
    set_path(tmp_path)

    folder = tmp_path.joinpath('i18n', 'en')
    folder.mkdir(parents=True)

    folder.joinpath('valid.json').write_text(json.dumps({"hello": "world"}))

    assert __load_file('en', 'valid') == {"hello": "world"}


def test_load_file_invalid(tmp_path):
    set_path(tmp_path)

    folder = tmp_path.joinpath('i18n', 'en')
    folder.mkdir(parents=True)

    folder.joinpath('bad.json').write_text("{not valid")

    assert __load_file('en', 'bad') == {}
