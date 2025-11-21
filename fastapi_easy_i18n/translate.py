import json
import logging
import os
from pathlib import Path
from typing import Optional, Any, Dict, List

logging.basicConfig(level=logging.WARNING)
log = logging.getLogger('fastapi_easy_i18n')

I18N_PATHS: List[str] = [
    os.path.join(Path.cwd(), 'app', 'core', 'i18n'),
    os.path.join(Path(__file__).resolve().parent, 'core', 'i18n'),
]
_cache: Dict[str, Dict[str, str]] = {}


def set_path(path: str | Path, *, replace: bool = False) -> None:
    """
    Add or replace localization search paths relative to the project root.

    Examples:
        set_path('backend/app/core')               # add to search paths
        set_path('backend/app/core', replace=True) # replace all paths

    Args:
        path (str | Path): Path relative to the project root.
        replace (bool, optional): If True - replaces all existing paths (default False).
    """
    global I18N_PATHS

    full_path = str((Path.cwd() / Path(path) / 'i18n').resolve())

    if replace:
        I18N_PATHS.clear()
        I18N_PATHS.append(full_path)
    else:
        I18N_PATHS.insert(0, full_path)

    _cache.clear()


def __get_file_name(key: str) -> Optional[str]:
    return key.split('.', 1)[0] if '.' in key else None


def __get_key_name(key: str) -> Optional[str]:
    dot_index = key.find('.')
    return key[dot_index + 1:] if dot_index != -1 else None


def __load_file(locale: str, file_name: str) -> Dict[str, str]:
    cache_key = f"{locale}:{file_name}"

    if cache_key in _cache:
        return _cache[cache_key]

    for base_path in I18N_PATHS:
        file = os.path.join(base_path, locale, f"{file_name}.json")

        if not os.path.isfile(file):
            log.warning(f"File '{file_name}.json' for locale '{locale}' not found in: '{base_path}'")
            continue

        try:
            with open(file, encoding='utf-8-sig') as f:
                content = f.read().strip()
                if not content:
                    log.warning(f"Ignored empty JSON file: {file}")
                    continue

                data = json.loads(content)
                _cache[cache_key] = data
                return data
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            log.warning(f"Ignored invalid JSON file: {file}: {e}")

    return {}


def __translate_safe(key: str, params: Optional[dict[str, Any]] = None, *, locale: str) -> Optional[str]:
    if not (file_name := __get_file_name(key)) or not (key_name := __get_key_name(key)):
        return None

    try:
        messages = __load_file(locale, file_name)
        if not (message := messages.get(key_name)):
            return None

        if isinstance(message, str):
            try:
                return message.format(**(params or {}))
            except KeyError:
                return message
    except FileNotFoundError:
        return None
