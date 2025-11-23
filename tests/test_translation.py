import json

from unittest.mock import patch

from fastapi_easy_i18n import t, set_locale
from fastapi_easy_i18n.translate import I18N_PATHS, __translate_safe


def test_translation():
    assert t('pagination.next') == 'вперёд'


def test_translation_params():
    assert t('common.greeting', {'name': 'Aleksandro'}) == 'Привет, Aleksandro!'


def test_translation_en():
    set_locale('en')
    assert t('pagination.prev') == 'prev'


def test_translation_ru():
    set_locale('ru')
    assert t('pagination.prev') == 'назад'


def test_translate_safe_invalid_key():
    assert __translate_safe('nokey', locale='en') is None

    assert __translate_safe('file.', locale='en') is None

    assert __translate_safe('.key', locale='en') is None


def test_translate_safe_no_message(tmp_path):
    folder = tmp_path.joinpath('en')
    folder.mkdir()
    folder.joinpath('file.json').write_text(json.dumps({}))

    I18N_PATHS[:] = [str(tmp_path)]

    assert __translate_safe('file.key', locale='en') is None


def test_translate_safe_missing_format_param(tmp_path):
    folder = tmp_path.joinpath('en')
    folder.mkdir()
    folder.joinpath('f.json').write_text(json.dumps({"msg": "Hello {name}"}))

    I18N_PATHS[:] = [str(tmp_path)]
    assert __translate_safe('f.msg', locale='en') == 'Hello {name}'


def test_translate_safe_file_not_found(tmp_path):
    with patch('fastapi_easy_i18n.translate.__load_file', side_effect=FileNotFoundError):
        result = __translate_safe('missing.key', locale='en')

    assert result is None
