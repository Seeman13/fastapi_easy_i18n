# fastapi-easy-i18n
[🇬🇧 English](README.md) | [🇷🇺 Русский](README.ru.md)

**Простая, быстрая и полностью независимая библиотека для интернационализации (i18n) в FastAPI.**

Добавьте многоязычность в свой проект за пару минут. Никаких громоздких библиотек — только чистый Python и интуитивно понятный API.

[![PyPI version](https://badge.fury.io/py/fastapi-easy-i18n.svg)](https://pypi.org/project/fastapi-easy-i18n/)
[![Python Versions](https://img.shields.io/pypi/pyversions/fastapi-easy-i18n?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/github/license/Seeman13/fastapi-easy-i18n?color=yellow)](https://github.com/Seeman13/fastapi-easy-i18n/blob/main/LICENSE)
[![Build](https://github.com/Seeman13/fastapi-easy-i18n/actions/workflows/test-and-publish.yml/badge.svg?branch=main)](https://github.com/Seeman13/fastapi-easy-i18n/actions)
[![Coverage](https://img.shields.io/codecov/c/github/Seeman13/fastapi-easy-i18n?logo=codecov)](https://codecov.io/gh/Seeman13/fastapi-easy-i18n)
[![Downloads](https://pepy.tech/badge/fastapi-easy-i18n)](https://pepy.tech/project/fastapi-easy-i18n)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)

## 💡 Возможности

* 🔧 Минимальная настройка
* ⚡ Быстрый доступ к переводам
* 🌍 Глобальная и локальная установка языка
* 📝 Поддержка параметров в строках
* 📦 Без внешних зависимостей

---

## 📥 Установка

```bash
pip install fastapi-easy-i18n
```

## 🚀 Использование

### Базовый пример

```python
from fastapi_easy_i18n import t, set_locale

set_locale('en')
print(t('common.hello'))  # → Hello!
```

## 🌐 Управление локалями

### Установка глобальной локали

По умолчанию используется `'ru'`.

```python
set_locale('it')
print(get_locale())  # → 'it'

set_locale('fr')
print(get_locale())  # → 'fr'
```

**Аргументы:**

* `locale`: код локали (`'ru'`, `'en'`, `'it'`, `'de'`, `'fr'`, ...)

---

### Получение текущей локали

```python
print(get_locale())  # → 'ru'
set_locale('en')
print(get_locale())  # → 'en'
```

---

### Временная локаль (context manager)

Используется для локального изменения языка внутри блока:

```python
with locale_context('en'):
    print(t('common.hello'))  # → Hello!

# после выхода локаль восстановится автоматически
```

---

## ✨ Функции перевода строк

Переводит сообщение для выбранной локали.

```python
t(key, params=None, locale=None)
```

```python
# alias
_(key, params=None, locale=None)
```

### Параметры:

* **key** — ключ вида `"file.key"`
  Например: `"pagination.next"`, `"errors.not_found"`
* **params** — словарь параметров для форматирования строки
  Например: `{'name': 'Alice'}`
* **locale** — локаль для конкретного вызова (необязательно)

### Примеры:

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

## 📁 Структура переводов

Создайте в Вашем проекте следующую структуру каталогов где будут храниться файлы переводов:

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

Если архитектура Вашего приложения отличается, Вы можете выбрать абсолютно любой каталог для хранения файлов переводов.

Для этого просто сообщите библиотеке об этом, вызвав метод ```set_patch('patch')```, например:

```python
set_path('backend/app/core')               # добавить новый каталог с файлами переводов
set_path('backend/app/core', replace=True) # заменить все каталоги с файлами переводов
```

---
