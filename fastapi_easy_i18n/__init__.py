from contextlib import contextmanager
from typing import Generator

from .translate import set_path, __translate_safe

_locale: str = 'ru'


def set_locale(locale: str) -> None:
    """
    Set global locale (default 'ru').

    Args:
        locale: Locale code to set as global default (e.g., 'ru', 'en', 'it', 'de', 'fr')

    Examples:
        >>> set_locale('en')
        >>> get_locale()
        'en'

        >>> set_locale('fr')
        >>> get_locale()
        'fr'
    """
    global _locale
    _locale = locale


def get_locale() -> str:
    """
    Get current global locale.

    Returns:
        Current global locale code.

    Examples:
        >>> get_locale()
        'ru'

        >>> set_locale('en')
        >>> get_locale()
        'en'
    """
    return _locale


@contextmanager
def locale_context(locale: str) -> Generator[None, None, None]:
    """
     Context manager for temporary locale setting.

     Temporarily sets the locale within the context block,
     then automatically restores the previous locale.

     Args:
         locale: Temporary locale code to use within context

     Examples:
         >>> with locale_context('en'):
         ...     print(t('common.hello'))  # Uses 'en' locale
         >>> # Automatically reverts to previous locale
     """
    global _locale
    old_locale = _locale
    _locale = locale
    try:
        yield
    finally:
        _locale = old_locale


def t(key: str, params: dict | None = None, *, locale: str | None = None) -> str:
    """
    Translation of messages in the selected localization.

    Args:
        key: Translation key in format 'file_name.key_name'.
             For example: 'pagination.next', 'errors.not_found'
        params: Optional dictionary with parameters for string formatting.
                For example: {'name': 'Aleksandro'} for message "Hello, {name}!"
        locale: Optional locale code. If not provided, uses locale default 'ru' or use global locale if it was set.

    Returns:
        Translated string if found, otherwise the original key.

    Examples:
        >>> t('pagination.next')
        'вперёд'

        >>> t('common.greeting', {'name': 'Alice'})
        'Hello, Alice!'

        >>> t('common.hello', locale='en')
        'Hello'

        >>> t('unknown.key')
        'unknown.key'
    """
    target_locale = locale or _locale
    return __translate_safe(key, params, locale=target_locale) or key


_ = t
__all__ = ['set_path', 'set_locale', 'get_locale', 'locale_context', 't', '_']
