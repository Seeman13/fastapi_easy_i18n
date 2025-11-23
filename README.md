# FastAPI Easy i18n

[🇷🇺 Русский](README.ru.md) | [🇬🇧 English](README.md)

**A simple, fast, and fully independent internationalization (i18n) library for FastAPI.**

Add multilingual support to your project in just a few minutes. No heavy libraries — only pure Python and an intuitive API.

[![PyPI version](https://badge.fury.io/py/fastapi-easy-i18n.svg)](https://pypi.org/project/fastapi-easy-i18n/)
[![Python Versions](https://img.shields.io/pypi/pyversions/fastapi-easy-i18n?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/github/license/Seeman13/fastapi_easy_i18n?color=yellow)](https://github.com/Seeman13/fastapi-easy-i18n/blob/main/LICENSE)
[![Build](https://github.com/Seeman13/fastapi-easy-i18n/workflows/publish/badge.svg?branch=main)](https://github.com/Seeman13/fastapi-easy-i18n/actions)
[![codecov](https://codecov.io/gh/Seeman13/fastapi_easy_i18n/branch/main/graph/badge.svg)](https://codecov.io/gh/Seeman13/fastapi_easy_i18n)
[![Downloads](https://pepy.tech/badge/fastapi-easy-i18n)](https://pepy.tech/project/fastapi-easy-i18n)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)

## 💡 Features

* 🔧 Minimal setup
* ⚡ Fast access to translations
* 🌍 Global and local locale setting
* 📝 String parameter support
* 📦 No external dependencies

---

## 📥 Installation

```bash
pip install fastapi-easy-i18n
```

## 🚀 Usage

### Basic example

```python
from fastapi_easy_i18n import t, set_locale

set_locale('en')
print(t('common.hello'))  # → Hello!
```

## 🌐 Locale Management

### Sett a global locale

The default use locale `'ru'`.

```python
set_locale('it')
print(get_locale())  # → 'it'

set_locale('fr')
print(get_locale())  # → 'fr'
```

**Arguments:**

* `locale`: locale code (`'ru'`, `'en'`, `'it'`, `'de'`, `'fr'`, ...)

---

### Get the current locale

```python
print(get_locale())  # → 'ru'
set_locale('en')
print(get_locale())  # → 'en'
```

---

### Temp locale (context manager)

Used for temporarily changing the locale within a block:

```python
with locale_context('en'):
    print(t('common.hello'))  # → Hello!

# after exiting, the locale is restored automatically
```

---

## ✨ Translation Functions

Translates a message for the selected locale.

```python
t(key, params=None, locale=None)
```

```python
# alias
_(key, params=None, locale=None)
```

### Parameters:

* **key** — key in the format `"file.key"`
  For example: `"pagination.next"`, `"errors.not_found"`
* **params** — dictionary of parameters for string formatting
  For example: `{'name': 'Alice'}`
* **locale** — locale for this specific call (optional)

### Examples:

```python
t('pagination.next')
# → 'вперёд'

t('common.greeting', {'name': 'Alice'})
# → 'Привет, Alice!'

_('pagination.next', locale='en')
# → 'next'

_('unknown.key')
# → 'unknown.key'
```

---

## 📁 Translation File Structure

Create the following directory structure in your project to store translation files:

```tree
your_fastapi_project/
└── app/
    └── core/
        └── i18n/
            ├── en/
            │   ├── common.json
            │   ├── errors.json
            │   └── pagination.json
            └── ru/
                ├── common.json
                ├── errors.json
                └── pagination.json
```

If your application architecture is different, you can choose any directory  to store translation files.

Simply inform the library about it by calling the ```set_patch('patch')``` method, for example:

```python
set_path('backend/app/core')               # add to search paths
set_path('backend/app/core', replace=True) # replace all paths
```

---
