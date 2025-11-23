from fastapi_easy_i18n import t, set_locale, get_locale


def test_set_locale():
    set_locale('en')
    assert t('pagination.prev') == 'prev'
    set_locale('ru')


def test_get_locale():
    assert get_locale() == 'ru'


def test_locale_context():
    from fastapi_easy_i18n import locale_context
    with locale_context('en'):
        assert t('pagination.next') == 'next'

    assert t('pagination.next') == 'вперёд'
