import pytest

from pathlib import Path

from fastapi_easy_i18n import set_path
from fastapi_easy_i18n.translate import I18N_PATHS, _cache


@pytest.fixture(autouse=True)
def reset_paths():
    original_paths = I18N_PATHS.copy()
    I18N_PATHS.clear()

    yield

    I18N_PATHS.clear()
    I18N_PATHS.extend(original_paths)


def test_set_path():
    _cache['dummy'] = {'key': 'value'}

    set_path('backend/app/core')

    assert I18N_PATHS[0] == str((Path.cwd() / 'backend/app/core/i18n').resolve())
    assert _cache == {}


def test_set_path_replace():
    _cache['dummy'] = {'key': 'value'}

    I18N_PATHS.extend(['some/old/path'])

    set_path('backend/app/core', replace=True)
    path = str((Path.cwd() / 'backend/app/core/i18n').resolve())

    assert I18N_PATHS == [path]
    assert _cache == {}


def test_set_path_multiple():
    set_path('path1')
    set_path('path2')

    path1 = str((Path.cwd() / 'path1/i18n').resolve())
    path2 = str((Path.cwd() / 'path2/i18n').resolve())

    assert I18N_PATHS == [path2, path1]
