### Hexlet tests and linter status:
[![Actions Status](https://github.com/Heilig-Di/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Heilig-Di/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/aad2cd9c3bae369086a0/maintainability)](https://codeclimate.com/github/Heilig-Di/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/aad2cd9c3bae369086a0/test_coverage)](https://codeclimate.com/github/Heilig-Di/python-project-50/test_coverage)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Heilig-Di_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Heilig-Di_python-project-50)

# Привет!
### Это вычислитель отличий
Утилита принимает два файла в формате .json или .yaml (на выбор), сравнивает их, анализирует и показывает разницу.

Ты можешь увидеть вывод в трех разных форматах:
- Древовидные структуры (stylish, по умолчанию)
- Текстовый (plain)
- JSON-формат (json)

Можешь ознакомиться с примерами работы.
#### Stylish
[![asciicast](https://asciinema.org/a/hwm0lYK5tdfnNGuGP7g9VczOj.svg)](https://asciinema.org/a/hwm0lYK5tdfnNGuGP7g9VczOj)
#### Stylish (.yaml)
[![asciicast](https://asciinema.org/a/vjAePy95NPNOfKuJz6aokplMo.svg)](https://asciinema.org/a/vjAePy95NPNOfKuJz6aokplMo)
#### Plain
[![asciicast](https://asciinema.org/a/o0TfKGKJE27Aigq3FxjAmrUzH.svg)](https://asciinema.org/a/o0TfKGKJE27Aigq3FxjAmrUzH)
#### Json
[![asciicast](https://asciinema.org/a/Nx1DHTt7Jj7S9iNPZEKDwc9nP.svg)](https://asciinema.org/a/Nx1DHTt7Jj7S9iNPZEKDwc9nP)

## Использование
Чтобы установить проект, клонируйте репозиторий.
```
git clone https://github.com/Heilig-Di/python-project-50.git
```
Для установки зависимостей запустите:
```
uv pip install -e ".[dev]"
```
Для удаления запустите:
```
rm -rf python-project-50
```
Чтобы переустановить пакет, сначала удалите его.
Затем повторите шаги по установке.
## Технологии
- Python 3.12
- Makefile 1.1.0
- Pytest 5.0.0
- Ruff 0.9.10

**Надеюсь было полезно!**
